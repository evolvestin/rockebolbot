import logging
import os
import re
import sys
import traceback
from datetime import datetime, timezone
from typing import Any

from aiogram import Bot, types

from services.bot_info import BotInfo
from services.config import ID_DEV, IGNORE_ERRORS_PATTERN
from services.functions import bold, code, html_link, html_secure, italic, sub_tag


def extract_error_details() -> tuple[str, list[str]]:
    """Extracts detailed information about the current exception."""
    exc_type, exc_value, exc_traceback = sys.exc_info()
    error_raw = traceback.format_exception(exc_type, exc_value, exc_traceback)
    return ''.join([html_secure(e) for e in error_raw]), error_raw


class TelegramError:
    """Class for handling and sending error reports to Telegram."""

    def __init__(self, bot: Bot) -> None:
        self.bot = bot
        self.header = self.build_header()
        self.dev_chat_id = ID_DEV

    @staticmethod
    def build_header() -> str:
        """Constructs a header for error messages."""
        host = 'local' if os.getenv('LOCAL') else 'server'
        link = html_link(f'https://t.me/{BotInfo.username}', BotInfo.username)
        return f'{bold(link)} ({italic(host)})'

    async def send_error_report(self, error: str, message: Any = None) -> None:
        """Sends an error report to the developer chat."""
        caption, reply_id = None, None
        title = f'Вылет {self.header}:\n'
        len_error_text = len(sub_tag(title)) + len(error)

        if message:
            caption = f'{title}{code(error)}' if 0 < len_error_text <= 1024 else None
            file_name = f'error_report_{datetime.now(timezone.utc).strftime("%Y-%m-%d_%H-%M-%S")}.json'
            file = types.BufferedInputFile(str(message).encode('utf-16'), filename=file_name)
            response = await self.bot.send_document(
                chat_id=self.dev_chat_id, document=file, caption=caption, parse_mode='HTML'
            )
            reply_id = response.message_id if response else reply_id

        if not caption:
            step = 4096 - len(sub_tag(title))
            for text in [error[i : i + step] for i in range(0, len(error), step)]:
                response = await self.bot.send_message(
                    chat_id=self.dev_chat_id,
                    text=f'{title}{code(text)}',
                    reply_to_message_id=reply_id,
                    parse_mode='HTML',
                )
                title = ''
                reply_id = response.message_id if response else reply_id

    async def handle_error(self, event: types.ErrorEvent) -> None:
        """Handles the current exception by reporting it."""
        error, error_raw = extract_error_details()
        message = None

        try:
            logging.error(f'Error {event} {error_raw[-1]}')
            if re.search(IGNORE_ERRORS_PATTERN, error):
                return
            await self.send_error_report(error, message or '')
        except Exception as short_error:
            more_error, _ = extract_error_details()
            error_text = f'FIRST ERROR:\n\n{error}\n\nMORE SHORT ERROR: {short_error}\nMORE ERROR:\n\n{more_error}'
            file = types.BufferedInputFile(error_text.encode('utf-16'), filename='error_report_fatal.json')
            await self.bot.send_document(chat_id=self.dev_chat_id, document=file, caption='FATAL ERROR #fatal')
