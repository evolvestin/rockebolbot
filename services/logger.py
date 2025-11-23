import re
from datetime import datetime, timezone
from typing import Optional, Union

from aiogram import Bot, types

from services.bot_info import BotInfo
from services.config import ID_FORWARD, ID_LOGS, ID_MEDIA
from services.functions import blockquote, bold, code, html_link, html_secure


class EntitiesToHTML:
    """Handles the conversion of message entities into HTML tags for formatting purposes."""

    def __init__(self, message: types.Message):
        self.message: types.Message = message

    @staticmethod
    def generate_html_tags(entity: types.MessageEntity) -> tuple[str, str]:
        """Generates HTML opening and closing tags based on the entity type."""
        if entity.type == 'pre':
            if entity.language:
                return f'<pre><code class="language-{entity.language}">', '</code></pre>'
            else:
                return '<pre>', '</pre>'

        if entity.type in ['url', 'email', 'cashtag', 'hashtag', 'mention', 'phone_number', 'text_mention']:
            return '', ''

        html_tags_by_type = {
            'bold': ('<b>', '</b>'),
            'italic': ('<i>', '</i>'),
            'underline': ('<u>', '</u>'),
            'code': ('<code>', '</code>'),
            'strikethrough': ('<s>', '</s>'),
            'spoiler': ('<tg-spoiler>', '</tg-spoiler>'),
            'blockquote': ('<blockquote>', '</blockquote>'),
            'text_link': (f'<a href="{entity.url}">', '</a>'),
            'expandable_blockquote': ('<blockquote expandable>', '</blockquote>'),
        }
        return html_tags_by_type.get(entity.type) or html_tags_by_type['code']

    def convert(self) -> str:
        """Converts message entities to an HTML formatted string."""
        entities = self.message.entities or self.message.caption_entities
        text_list = list(self.message.text or self.message.caption or [])
        if entities:
            position = 0
            for entity in text_list:
                true_length = len(entity.encode('utf-16-le')) // 2
                while true_length > 1:
                    text_list.insert(position + 1, '')
                    true_length -= 1
                position += 1
            for entity in reversed(entities):
                end_index = entity.offset + entity.length - 1
                if entity.offset + entity.length >= len(text_list):
                    end_index = len(text_list) - 1

                tag_start, tag_end = self.generate_html_tags(entity)
                text_list[entity.offset] = f'{tag_start}{text_list[entity.offset]}'
                text_list[end_index] += tag_end
        return ''.join(text_list)


class ChatMemberLogHandler:
    """Handles logging of chat member updates in Telegram chats."""

    PERMISSIONS_MAP = {
        'can_manage_chat': 'управлять {chat_type}ом',
        'can_post_messages': 'отправлять сообщения',
        'can_edit_messages': 'редактировать сообщения',
        'can_delete_messages': 'удалять сообщения',
        'can_restrict_members': 'банить пользователей',
        'can_post_stories': 'публиковать истории',
        'can_edit_stories': 'редактировать истории',
        'can_delete_stories': 'удалять истории',
        'can_manage_video_chats': 'управлять видео чатами',
        'can_promote_members': 'назначать пользователей админом',
        'can_manage_voice_chats': 'управлять голосовыми чатами',
        'can_be_edited': 'бот редактировать этого {user_type}',
        'can_send_messages': 'отправлять сообщения',
        'can_send_photos': 'отправлять фотографии',
        'can_send_videos': 'отправлять видео',
        'can_send_video_notes': 'отправлять видео-сообщение',
        'can_send_audios': 'отправлять аудио',
        'can_send_voice_notes': 'отправлять голосовые сообщения',
        'can_send_documents': 'отправлять документы',
        'can_send_other_messages': 'отправлять стикеры и анимации',
        'can_send_media_messages': 'отправлять медиа сообщения',
        'can_add_web_page_previews': 'добавлять пред-просмотры ссылок',
        'can_send_polls': 'отправлять опросы',
        'can_invite_users': 'добавлять пользователей',
        'can_manage_topics': 'управлять темами форума',
        'can_pin_messages': 'закреплять сообщения',
        'can_change_info': 'изменять информацию о {chat_type}е',
    }

    def __init__(self, message: types.ChatMemberUpdated):
        self.message: types.ChatMemberUpdated = message
        self.old_member = message.old_chat_member
        self.new_member = message.new_chat_member
        self.old_status = message.old_chat_member.status
        self.new_status = message.new_chat_member.status
        self.ru_user_type = 'бота' if message.new_chat_member.user.is_bot else 'пользователя'
        self.ru_chat_type = 'канал' if message.chat.type == 'channel' else 'чат'

    def get_action_for_old_member(self) -> tuple[str, str]:
        """Determines the action and hashtag based on the old member status."""
        if self.old_status in ['left', 'kicked']:
            if self.message.chat.id < 0:
                return self.handle_chat_entry_or_kick()
            return f'Разблокировал {self.ru_user_type}', 'unblocked'
        else:
            if self.message.chat.id < 0:
                return self.handle_chat_removal_or_change()
            return f'Заблокировал {self.ru_user_type}', 'block'

    def handle_chat_entry_or_kick(self) -> tuple[str, str]:
        """Handles logic for user entry or kick events."""
        if self.new_status == 'left':
            return f'Разрешил вход {self.ru_user_type} в {self.ru_chat_type}', 'changed'
        elif self.new_status == 'kicked':
            return f'Запретил вход {self.ru_user_type} в {self.ru_chat_type}', 'changed'
        elif self.new_status == 'administrator':
            return f'Добавил {self.ru_user_type} как админа в {self.ru_chat_type}', 'added'
        return f'Добавил {self.ru_user_type} в {self.ru_chat_type}', 'added'

    def handle_chat_removal_or_change(self) -> tuple[str, str]:
        """Handles logic for user removal or permission changes."""
        if self.new_status in ['left', 'kicked']:
            admin = '-админа' if self.old_status == 'administrator' else ''
            return f'Удалил {self.ru_user_type}{admin} из {self.ru_chat_type}а', 'kicked'
        elif self.old_status == 'administrator' and self.new_status == 'administrator':
            return f'Изменил {self.ru_user_type} как админа в {self.ru_chat_type}е', 'changed'
        elif self.new_status == 'administrator':
            return f'Назначил {self.ru_user_type} админом в {self.ru_chat_type}е', 'changed'
        elif self.old_status == 'restricted' and self.new_status == 'restricted':
            return f'Изменил ограничения {self.ru_user_type} в {self.ru_chat_type}е', 'changed'
        elif self.old_status == 'restricted' and self.new_status != 'restricted':
            return f'Снял ограничения {self.ru_user_type} в {self.ru_chat_type}е', 'changed'
        elif self.new_status == 'restricted':
            return f'Ограничил {self.ru_user_type} в {self.ru_chat_type}е', 'changed'
        return f'Забрал роль админа у {self.ru_user_type} в {self.ru_chat_type}е', 'changed'

    def compare_permissions(self) -> str:
        """Compares old and new permissions to generate a difference report."""
        changes = []
        format_ctx = {'chat_type': self.ru_chat_type, 'user_type': self.ru_user_type}

        if self.old_status == self.new_status:
            for permission, desc_template in self.PERMISSIONS_MAP.items():
                old_val = getattr(self.message.old_chat_member, permission, None)
                new_val = getattr(self.message.new_chat_member, permission, None)

                if old_val is not None and new_val is not None and old_val != new_val:
                    description = desc_template.format(**format_ctx)
                    action = 'Разрешил' if new_val else 'Запретил'
                    changes.append(bold(f'{action} {description} #{permission}'))

        elif self.new_status in ['administrator', 'restricted']:
            for permission, desc_template in self.PERMISSIONS_MAP.items():
                new_val = getattr(self.message.new_chat_member, permission, None)
                if new_val is not None:
                    description = desc_template.format(**format_ctx)
                    state = 'Может' if new_val else 'Не может'
                    changes.append(bold(f'{state} {description} #{permission}'))

        return '\n'.join(changes) or ''

    def handle_self_action(self) -> tuple[str, str]:
        """Handles actions performed by the user on themselves (e.g., joining/leaving)."""
        if self.old_status in ['left', 'kicked']:
            return f'Зашел в {self.ru_chat_type} по ссылке', 'added'
        return f'Вышел из {self.ru_chat_type}а', 'left'


class ProcessMessage:
    """Handles processing of various types of messages in Telegram."""

    def __init__(self, message: types.Message):
        self.message: types.Message = message

    def get_media_file_id_and_description(self) -> tuple[Optional[str], str]:
        """Retrieves the file ID and a description for media messages."""
        if self.message.photo:
            return self.message.photo[-1].file_id, f'{bold("Отправил фото")} #photo'
        elif self.message.new_chat_photo:
            return self.message.new_chat_photo[-1].file_id, f'{bold("Изменил аватар чата")} #new_chat_photo'
        elif self.message.animation:
            return self.message.animation.file_id, f'{bold("Отправил анимацию")} #gif #animation'
        elif self.message.document:
            return self.message.document.file_id, f'{bold("Отправил документ")} #document'
        elif self.message.voice:
            return self.message.voice.file_id, f'{bold("Отправил голосовое сообщение")} #voice'
        elif self.message.audio:
            return self.message.audio.file_id, f'{bold("Отправил аудиофайл")} #audio'
        elif self.message.video:
            return self.message.video.file_id, f'{bold("Отправил видео")} #video'
        elif self.message.video_note:
            return self.message.video_note.file_id, f'{bold("Отправил видео-сообщение")} #video_note'
        elif self.message.sticker:
            return self.message.sticker.file_id, f'{bold("Отправил стикер")} #sticker'
        elif self.message.paid_media:
            return None, f'{bold(f"Отправил платный медиа")} за {self.message.paid_media.star_count}⭐ #paid_media'
        elif self.message.story:
            return None, f'{bold("Опубликовал историю")} #story'
        elif self.message.dice:
            return None, f'{bold("Отправил дайс")} {self.message.dice.emoji}: {self.message.dice.value} #dice'
        elif self.message.poll:
            return None, f'Создал {bold("викторину" if self.message.poll.type == "quiz" else "голосование")} #poll'
        elif self.message.location:
            return None, f'{bold("Отправил локацию")} #location'
        elif self.message.venue:
            return None, f'{bold("Отправил место")} #venue'
        elif self.message.contact:
            return None, f'{bold("Отправил контакт")} #contact'
        elif self.message.game:
            return None, f'{bold("Запустил игру")} #game'
        elif self.message.chat_background_set:
            return None, f'{bold("Изменил фон чата")} #chat_background_set'
        else:
            return None, f'{bold("Неизвестное действие")} #unknown #{self.message.content_type}'

    def get_chat_action_description(self) -> Optional[str]:
        """Retrieves a description for service messages (e.g., chat title change)."""
        if self.message.new_chat_title:
            return f'{bold("Изменил название чата")} #new_chat_title'
        elif self.message.delete_chat_photo:
            return f'{bold("Удалил аватар чата")} #delete_chat_photo'
        elif self.message.left_chat_member:
            return f'{bold("Участник покинул чат")} #left_chat_member'
        elif self.message.connected_website:
            return f'{bold("Подключил веб-сайт")} #connected_website'
        elif self.message.new_chat_members:
            return f'{bold("Добавил новых участников в чат")} #new_chat_members'
        elif self.message.write_access_allowed:
            return f'{bold("Предоставил доступ к записи")} #write_access_allowed'
        elif self.message.message_auto_delete_timer_changed:
            return f'{bold("Изменил таймер авто-удаления сообщений")} #auto_delete_timer_changed'
        elif self.message.group_chat_created:
            return f'{bold("Создал группу")} #group_chat_created'
        elif self.message.supergroup_chat_created:
            return f'{bold("Создал супергруппу")} #supergroup_chat_created'
        elif self.message.channel_chat_created:
            return f'{bold("Создал канал")} #channel_chat_created'
        elif self.message.migrate_to_chat_id:
            return f'{bold("Чат деактивирован:")} #chat_upgrade\nНовый ID: {code(self.message.migrate_to_chat_id)}'
        elif self.message.migrate_from_chat_id:
            return (
                f'{bold("Чат стал супергруппой:")} #chat_upgraded\nСтарый ID: {code(self.message.migrate_from_chat_id)}'
            )
        elif self.message.forum_topic_created:
            return f'{bold("Создал тему форума")} #forum_topic_created'
        elif self.message.forum_topic_edited:
            return f'{bold("Отредактировал тему форума")} #forum_topic_edited'
        elif self.message.forum_topic_closed:
            return f'{bold("Закрыл тему форума")} #forum_topic_closed'
        elif self.message.forum_topic_reopened:
            return f'{bold("Открыл тему форума")} #forum_topic_reopened'
        elif self.message.general_forum_topic_hidden:
            return f'{bold("Скрыл общую тему форума")} #general_forum_topic_hidden'
        elif self.message.general_forum_topic_unhidden:
            return f'{bold("Открыл общую тему форума")} #general_forum_topic_unhidden'
        elif self.message.proximity_alert_triggered:
            return f'{bold("Сработал proximity alert")} #proximity_alert_triggered'
        elif self.message.video_chat_scheduled:
            return f'{bold("Запланировал видеочат")} #video_chat_scheduled'
        elif self.message.video_chat_started:
            return f'{bold("Начал видеочат")} #video_chat_started'
        elif self.message.video_chat_participants_invited:
            return f'{bold("Пригласил участников в видеочат")} #video_chat_participants_invited'
        elif self.message.video_chat_ended:
            return f'{bold("Завершил видеочат")} #video_chat_ended'
        elif self.message.invoice:
            return f'{bold("Отправил счет")} #invoice'
        elif self.message.successful_payment:
            return f'{bold("Произвел успешный платеж")} #successful_payment'
        elif self.message.refunded_payment:
            return f'{bold("Возврат платежа")} #refunded_payment'
        elif self.message.giveaway:
            return f'{bold("Создал розыгрыш")} #giveaway'
        elif self.message.giveaway_winners:
            return f'{bold("Определены победители розыгрыша")} #giveaway_winners'
        elif self.message.giveaway_completed:
            return f'{bold("Розыгрыш завершён")} #giveaway_completed'
        elif self.message.boost_added:
            return f'{bold("Забустил")} #boost_added'
        elif self.message.user_shared:
            return f'{bold("Поделился пользователем")} #user_shared'
        elif self.message.users_shared:
            return f'{bold("Поделился пользователями")} #users_shared'
        elif self.message.chat_shared:
            return f'{bold("Поделился чатом")} #chat_shared'
        elif self.message.passport_data:
            return f'{bold("Отправил данные паспорта")} #passport_data'
        elif self.message.web_app_data:
            return f'{bold("Отправил данные веб-приложения")} #web_app_data'
        else:
            return None


class TelegramLogger:
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @staticmethod
    def get_header(chat: Union[types.Chat, types.User], date: datetime = None) -> str:
        """Constructs a formatted header string with chat/user details."""
        parts = []
        if date:
            parts.append(code(date.strftime('%Y-%m-%d %H:%M:%S')))
        parts.append(html_secure(chat.full_name))
        if chat.username:
            parts.append(f'[@{chat.username}]')
        if chat.id:
            parts.append(code(chat.id))
        return ' '.join(parts)

    @staticmethod
    def channel_link(message: types.Message) -> str:
        """Generates a link to a message in a channel or chat."""
        link = message.chat.username or re.sub('-100', '', f'c/{message.chat.id}')
        return f'https://t.me/{link}/{message.message_id}'

    async def process_media_message(
        self,
        message: types.Message,
        header_parts: list,
    ) -> tuple[list, Optional[str]]:
        """Processes media messages, forwarding them to the media channel if configured."""
        caption_text = EntitiesToHTML(message).convert()
        file_id, description = ProcessMessage(message).get_media_file_id_and_description()
        file_id_line = f'FILE_ID: {code(file_id)}' if file_id else None

        media = None
        try:
            if message.caption and len(message.caption) > 1024:
                media = await self.bot.forward_message(
                    chat_id=ID_MEDIA, from_chat_id=message.chat.id, message_id=message.message_id
                )
            else:
                media_id_obj = await self.bot.copy_message(
                    chat_id=ID_MEDIA,
                    from_chat_id=message.chat.id,
                    message_id=message.message_id,
                    caption=caption_text,
                    parse_mode='HTML',
                )
                media = types.Message(
                    message_id=media_id_obj.message_id,
                    date=datetime.now(),
                    chat=types.Chat(id=ID_MEDIA, type='channel'),
                )
        except Exception:
            pass

        if media:
            header_parts.append(self.channel_link(media))

            if isinstance(message.forward_origin, types.MessageOriginChannel):
                forwarded_media_message = types.Message(
                    date=datetime.now(),
                    chat=message.forward_origin.chat,
                    message_id=message.forward_origin.message_id,
                )
                header_parts.append(self.channel_link(forwarded_media_message))

            if message.sticker:
                header_parts.append(f'https://t.me/addstickers/{message.sticker.set_name}')
            elif message.contact and message.contact.user_id:
                header_parts.append(f'ID пользователя: {code(message.contact.user_id)}')

            header_parts.append(file_id_line) if file_id_line else None
            header_parts.append(f'{description} #media{" с текстом:" if caption_text else ""}')

            header = '\n'.join([f'{BotInfo.username}:'] + header_parts)
            try:
                await self.bot.send_message(
                    chat_id=ID_MEDIA, text=blockquote(header), reply_to_message_id=media.message_id, parse_mode='HTML'
                )
            except Exception:
                pass

        return header_parts, caption_text

    async def log_message_handler(
        self, message: types.Message, from_user: types.User, include_details: bool = True
    ) -> tuple[str, Optional[str]]:
        """Generates the log header and body for a message."""
        message_body, forwarded_from = None, None
        action_date = message.date if include_details else datetime.now(timezone.utc)
        header_parts = [f'{self.get_header(message.chat, action_date)}:']

        if isinstance(message, types.Message):
            if isinstance(message.forward_origin, types.MessageOriginChat):
                forwarded_from = message.forward_origin.sender_chat
            elif isinstance(message.forward_origin, types.MessageOriginUser):
                forwarded_from = message.forward_origin.sender_user
            elif isinstance(message.forward_origin, types.MessageOriginChannel):
                forwarded_from = message.forward_origin.chat
            elif isinstance(message.forward_origin, types.MessageOriginHiddenUser):
                forwarded_from = types.User(id=0, first_name=message.forward_origin.sender_user_name, is_bot=False)
        else:
            include_details = False
            header_parts.append(f'{message.message_id} #inaccessible')

        if message.chat.id < 0 and from_user:
            header_parts.append(f'👤 {self.get_header(from_user)}:')

        if forwarded_from:
            try:
                forwarded_message = await self.bot.forward_message(
                    chat_id=ID_FORWARD, from_chat_id=message.chat.id, message_id=message.message_id
                )
                header_parts.append(
                    f'{html_link(self.channel_link(forwarded_message), "Форвард")}'
                    f' от {self.get_header(chat=forwarded_from, date=message.forward_date)}:'
                )
            except Exception:
                header_parts.append(f'Форвард от {self.get_header(chat=forwarded_from)} (не удалось сохранить):')

        if include_details:
            if message.pinned_message:
                pinned_header, message_body = await self.log_message_handler(
                    message.pinned_message, message.from_user, include_details=True
                )
                header_parts.extend(
                    [
                        f'{bold("Закрепил сообщение:")} #pinned_message',
                        pinned_header,
                    ]
                )
            elif message.text:
                message_body = EntitiesToHTML(message).convert()
            else:
                action = ProcessMessage(message).get_chat_action_description()
                if action:
                    header_parts.append(action)
                else:
                    header_parts, message_body = await self.process_media_message(message, header_parts)
        header = '\n'.join(header_parts)
        return header, message_body

    async def chat_member(self, message: types.ChatMemberUpdated) -> str:
        """Generates log string for chat member updates."""
        member_text = ''
        header = f'{self.get_header(message.chat, message.date)}:\n'
        if message.chat.id < 0 and message.from_user:
            header += f'👤 {self.get_header(message.from_user)}:\n'

        new_member = message.new_chat_member.user
        chat_member_logger = ChatMemberLogHandler(message)

        if new_member.id != message.from_user.id:
            permissions = chat_member_logger.compare_permissions()
            action_text, action_hashtag = chat_member_logger.get_action_for_old_member()
            member_text = f'\n{"🤖" if new_member.is_bot else "👤"} {self.get_header(new_member)}'
            if permissions:
                member_text += f'\n{permissions}'
        else:
            action_text, action_hashtag = chat_member_logger.handle_self_action()
        return (
            f'{header}'
            f'{action_text} #{"bot" if new_member.is_bot else "user"}_{action_hashtag}'
            f'{" #me" if new_member.username == BotInfo.username else ""}'
            f'{member_text}'
        )

    async def send_log(self, text: str) -> None:
        """Sends the log text to the log channel, splitting if necessary."""
        try:
            if len(text) > 4096:
                for chunk in [text[i : i + 4096] for i in range(0, len(text), 4096)]:
                    await self.bot.send_message(ID_LOGS, chunk, parse_mode='HTML', disable_web_page_preview=True)
            else:
                await self.bot.send_message(ID_LOGS, text, parse_mode='HTML', disable_web_page_preview=True)
        except Exception as e:
            print(f'Logging error: {e}')

    async def log_message(self, message: types.Message) -> None:
        """Entry point for logging standard messages."""
        if message.chat.id in [ID_LOGS, ID_MEDIA, ID_FORWARD]:
            return

        log_header, log_body = await self.log_message_handler(message, message.from_user, include_details=True)
        full_log = log_header
        if log_body:
            full_log += f'\n{log_body}'
        await self.send_log(blockquote(full_log))

    async def log_chat_member_event(self, event: types.ChatMemberUpdated) -> None:
        """New entry point for ChatMemberUpdated events."""
        log_text = await self.chat_member(event)
        await self.send_log(blockquote(log_text))
