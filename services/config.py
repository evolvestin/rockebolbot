import os

from aiogram import Bot
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
dev_bot = Bot(token=os.getenv('DEV_TOKEN'))

ID_DEV = int(os.getenv('ID_DEV', 0))
ID_LOGS = int(os.getenv('ID_LOGS', 0))
ID_MEDIA = int(os.getenv('ID_MEDIA', 0))
ID_FORWARD = int(os.getenv('ID_FORWARD', 0))

VOICE_REACTION_ID = 'AwADAgADXAEAAu7TEEiU1v4upM88swI'
ADVICE_API_URL = 'https://fucking-great-advice.ru/api/random'

REACTION_TRIGGERS = set(os.getenv('REACTION', '').lower().split('/'))
BLACK_LIST_CHATS = set(os.getenv('BLACK_LIST', '').split(' '))

IGNORE_ERRORS_PATTERN = '|'.join(
    [
        'Backend Error',
        'Read timed out.',
        'Message_id_invalid',
        'Connection aborted',
        'ServerDisconnectedError',
        'Connection reset by peer',
        'is currently unavailable.',
        'returned "Internal Error"',
        'Message to forward not found',
        'Message can&#39;t be forwarded',
        'Failed to establish a new connection',
        'The (read|write) operation timed out',
        'EOF occurred in violation of protocol',
    ]
)

ALLOWED_UPDATES = [
    'callback_query',
    'channel_post',
    'chat_member',
    'edited_channel_post',
    'edited_message',
    'message',
    'my_chat_member',
]
