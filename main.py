import asyncio
import logging
import sys
from datetime import datetime, timezone

import aiohttp
from aiogram import Dispatcher, Router, types

from services.bot_info import BotInfo
from services.config import (
    ADVICE_API_URL,
    ALLOWED_UPDATES,
    BLACK_LIST_CHATS,
    ID_DEV,
    REACTION_TRIGGERS,
    VOICE_REACTION_ID,
    bot,
    dev_bot,
)
from services.error_handler import TelegramError
from services.functions import bold, code, html_secure
from services.logger import TelegramLogger

logger = TelegramLogger(bot)

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout, format='%(asctime)s [%(levelname)s] %(name)s: %(message)s')


async def handle_id_command(message: types.Message) -> None:
    """Handles the /id command, returning chat and user identifiers."""
    reply_parts = []

    if message.reply_to_message:
        target = message.reply_to_message.from_user
        reply_parts.append(logger.get_header(chat=target))
        reply_parts.append(f'ID: {code(target.id)}')
        reply_parts.append(f'Type: {bold("Bot" if target.is_bot else "User")}')
    else:
        reply_parts.append(f'Your ID: {code(message.from_user.id)}')
        if message.chat.id < 0:
            reply_parts.append(f'Chat ID: {code(message.chat.id)}')

    await message.reply(text='\n'.join(reply_parts), parse_mode='HTML')


async def get_random_advice() -> str:
    """Asynchronously retrieves a random piece of advice from an external API."""
    async with aiohttp.ClientSession() as session:
        async with session.get(ADVICE_API_URL, timeout=5) as response:
            data = await response.json()
            return html_secure(data.get('text', 'Нет совета :('))


async def all_messages_handler(message: types.Message) -> None:
    """Router for message processing logic."""
    if str(message.chat.id) not in BLACK_LIST_CHATS:
        asyncio.create_task(logger.log_message(message))

    if not message.text:
        return

    text_lower = message.text.lower()

    if text_lower.startswith('/id'):
        await handle_id_command(message)

    elif text_lower in REACTION_TRIGGERS:
        await message.reply_voice(voice=VOICE_REACTION_ID)

    elif 'совет' in text_lower:
        advice_text = await get_random_advice()
        await message.reply(text=advice_text, parse_mode='HTML')


def register_router() -> Router:
    """Registers all handlers into the router."""
    router = Router()

    router.my_chat_member.register(logger.log_chat_member_event)
    router.chat_member.register(logger.log_chat_member_event)
    router.errors.register(TelegramError(dev_bot).handle_error)
    router.message.register(all_messages_handler)
    return router


async def main() -> None:
    """Main entry point for the bot execution."""
    dispatcher = Dispatcher()
    dispatcher.include_router(register_router())

    await BotInfo.update_class_username(bot)
    try:
        header = logger.get_header(BotInfo.me)
        await dev_bot.send_message(
            chat_id=ID_DEV,
            text=f'{header}\n{code(datetime.now(tz=timezone.utc).strftime("%Y-%m-%d %H:%M:%S"))}',
            parse_mode='HTML',
        )
    except Exception as e:
        logging.error(f'Failed to send startup message: {e}')

    await dispatcher.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


if __name__ == '__main__':
    asyncio.run(main())
