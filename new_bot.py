import os
import _thread
import gspread
import requests
import functions
from SQL import SQL
from time import sleep
from aiogram import types
from copy import copy, deepcopy
from aiogram.utils import executor
from string import ascii_uppercase
from aiogram.dispatcher import Dispatcher
from datetime import datetime, timezone, timedelta
from functions import bold, code, italic, time_now
# =================================================================================================================
stamp1 = time_now()


def users_db_creation():
    db = SQL(db_path)
    spreadsheet = gspread.service_account('google.json').open('UNITED USERS')
    users = spreadsheet.worksheet(os.environ['sheet']).get('A1:Z50000', major_dimension='ROWS')
    raw_columns = db.create_table('users', users.pop(0), additional=True)
    users_ids, columns = db.upload('users', raw_columns, users)
    _zero_user = db.get_user(0)
    db.close()
    return _zero_user, ['id', *users_ids], columns


logging = []
idMe = 396978030
db_path = 'db/database.db'
functions.environmental_files()
os.makedirs('db', exist_ok=True)
tz = timezone(timedelta(hours=3))
Auth = functions.AuthCentre(LOG_DELAY=120,
                            ID_DEV=-1001312302092,
                            TOKEN=os.environ.get('TOKEN'),
                            ID_DUMP=os.environ.get('ID_DUMP'),
                            ID_LOGS=os.environ.get('ID_LOGS'),
                            ID_MEDIA=os.environ.get('ID_MEDIA'),
                            DEV_TOKEN=os.environ.get('DEV_TOKEN'))

bot = Auth.async_bot
dispatcher = Dispatcher(bot)
zero_user, google_users_ids, users_columns = users_db_creation()
black_list = [os.environ.get(key) for key in ['ID_DUMP', 'ID_MEDIA', 'ID_LOGS']]
black_list.extend(os.environ.get('black_list').split(' '))
# =================================================================================================================


def first_start(message):
    db = SQL(db_path)
    user = deepcopy(zero_user)
    _, name, username = Auth.logs.header(message['chat'].to_python())
    user.update({
        'name': name,
        'username': username,
        'id': message['chat']['id']})
    db.create_user(user)
    db.close()


async def sender(message, user, text=None, log_text=None, **a_kwargs):
    global logging
    dump = True if 'Впервые' in str(log_text) else None
    task = a_kwargs['func'] if a_kwargs.get('func') else bot.send_message
    kwargs = {'log': log_text, 'text': text, 'user': user, 'message': message, **a_kwargs}
    response, log_text, update = await Auth.async_message(task, **kwargs)
    if log_text is not None:
        logging.append(log_text)
        if dump:
            head, _, _ = Auth.logs.header(Auth.get_me)
            await Auth.async_message(bot.send_message, id=Auth.logs.dump_chat_id, text=f'{head}{log_text}')
    if update:
        db = SQL(db_path)
        db.update('users', user['id'], update)
        db.close()
    return response


@dispatcher.chat_member_handler()
@dispatcher.my_chat_member_handler()
async def member_handler(message: types.ChatMember):
    global logging
    try:
        db = SQL(db_path)
        user = db.get_user(message['chat']['id'])
        log_text, update, greeting = Auth.logs.chat_member(message, db.get_user(message['chat']['id']))
        if greeting and user is None:
            first_start(message)
        logging.append(log_text)
        db.update('users', message['chat']['id'], update) if update else None
        db.close()
    except IndexError and Exception:
        await Auth.dev.async_except(message)


@dispatcher.channel_post_handler()
async def repeat_channel_messages(message: types.Message):
    try:
        if str(message['chat']['id']) not in black_list:
            db = SQL(db_path)
            log_text = True
            user = db.get_user(message['chat']['id'])
            if user is None:
                first_start(message)
                log_text = ' [#Впервые]'
            await sender(message, user=user, log_text=log_text)
            db.close()
    except IndexError and Exception:
        await Auth.dev.async_except(message)


@dispatcher.message_handler(content_types=functions.red_contents)
async def red_messages(message: types.Message):
    try:
        if str(message['chat']['id']) not in black_list:
            db = SQL(db_path)
            user = db.get_user(message['chat']['id'])
            if user and message['migrate_to_chat_id']:
                db.update('users', user['id'], {'username': 'DISABLED_GROUP', 'reaction': '🅾️'})
            await sender(message, user, log_text=True)
            db.close()
    except IndexError and Exception:
        await Auth.dev.async_except(message)


@dispatcher.message_handler()
async def repeat_all_messages(message: types.Message):
    try:
        db = SQL(db_path)
        text, starting = None, None
        user = db.get_user(message['chat']['id'])
        log_text = True if str(message['chat']['id']) not in black_list else None
        if user is None:
            starting = True
            first_start(message)

        if message['text'].lower().startswith('/'):
            log_text = True
            if message['chat']['id'] == idMe:
                if message['text'].lower().startswith('/logs'):
                    text = Auth.logs.text()

                elif message['text'].lower().startswith('/reboot'):
                    text, log_text = Auth.logs.reboot(dispatcher)

            if message['text'].lower().startswith('/time'):
                text = f"{bold(Auth.time(form='iso'))} ({code('GMT+3')})"

            elif message['text'].lower().startswith('/id'):
                if message['reply_to_message']:
                    replied_type = 'Человек'
                    reply = message['reply_to_message']['from']
                    _, name, username = Auth.logs.header(reply.to_python())
                    if reply['is_bot']:
                        replied_type = 'Я' if reply['username'] == Auth.username else 'Бот'
                    text = f"{name} [{bold(f'@{username}')}]\n" + \
                           f"ID: {code(reply['id'])}\n" \
                           f"Тип: {bold(replied_type)}"
                else:
                    text = f"Your ID: {code(message['from']['id'])}\n"
                    if message['chat']['id'] < 0:
                        text += f"Group ID: {code(message['chat']['id'])}"

        elif message['text'].lower() in os.environ['reaction'].split('/'):
            file_id = 'AwADAgADXAEAAu7TEEiU1v4upM88swI'
            reply = message['reply_to_message']['message_id'] if message['reply_to_message'] else None
            await sender(message, user, log_text=log_text, func=bot.send_voice,
                         id=message['chat']['id'], file_id=file_id, reply=reply)
            log_text = None

        elif 'совет' in message['text'].lower():
            try:
                response = functions.make_dict(requests.get('http://fucking-great-advice.ru/api/random').text)
                reply = message['reply_to_message']['message_id'] if message['reply_to_message'] else None
                await sender(message, user, text=response.get('text'), log_text=log_text, reply=reply)
                log_text = None
            except IndexError and Exception as error:
                Auth.dev.printer(error)

        log_text = ' [#Впервые]' if starting else log_text
        await sender(message, user, text=text, log_text=log_text)
        db.close()
    except IndexError and Exception:
        await Auth.dev.async_except(message)


def google_update():
    global google_users_ids
    while True:
        try:
            sleep(2)
            db = SQL(db_path)
            users = db.get_updates()
            if len(users) > 0:
                client = gspread.service_account('google.json')
                worksheet = client.open('UNITED USERS').worksheet(os.environ['sheet'])
                for user in users:
                    del user['updates']
                    if str(user['id']) in google_users_ids:
                        text = 'обновлен'
                        row = google_users_ids.index(str(user['id'])) + 1
                    else:
                        text = 'добавлен'
                        row = len(google_users_ids) + 1
                        google_users_ids.append(str(user['id']))
                    google_row = f'A{row}:{ascii_uppercase[len(user)-1]}{row}'

                    try:
                        user_range = worksheet.range(google_row)
                    except IndexError and Exception as error:
                        if 'exceeds grid limits' in str(error):
                            worksheet.add_rows(1000)
                            user_range = worksheet.range(google_row)
                            sleep(5)
                        else:
                            raise error

                    for index, value, col_type in zip(range(len(user)), user.values(), users_columns):
                        value = Auth.time(value, form='iso', sep='_') if '<DATE>' in col_type else value
                        value = 'None' if value is None else value
                        user_range[index].value = value
                    worksheet.update_cells(user_range)
                    db.update('users', user['id'], {'updates': 0}, True)
                    Auth.dev.printer(f"Пользователь {text} {user['id']}")
                    sleep(1)
        except IndexError and Exception:
            Auth.dev.thread_except()


def detector():
    def advice_query():
        try:
            response = functions.make_dict(requests.get('http://fucking-great-advice.ru/api/random').text)
            return italic(functions.html_secure(response['text'])) if response.get('text') else '25'
        except IndexError and Exception:
            return '25'

    advice = advice_query()
    used = []
    while True:
        try:
            text = None
            date = datetime.now(tz)
            minute = date.strftime('%M')
            second = date.strftime('%S')
            if date.strftime('%H') in ['00', '08', '16'] and minute == '59':
                if second == '25' and second not in used:
                    text = advice
                    used.append(second)
                elif second in ['30', '35', '40', '45', '50', '55'] and second not in used:
                    used.append(second)
                    text = f'{minute}:{second}'

            if date.strftime('%H') in ['01', '09', '17'] and minute == '00' and second == '00':
                text = f'{minute}:{second}'

            if text:
                Auth.message(id=-1001376818013, text=text)
                if minute == '00' and second == '00':
                    advice = advice_query()
                    used.clear()
                    sleep(60)
            else:
                sleep(0.5)
        except IndexError and Exception:
            Auth.dev.thread_except()


def logger():
    global logging
    while True:
        try:
            log = copy(logging)
            logging = []
            Auth.logs.send(log)
        except IndexError and Exception:
            Auth.dev.thread_except()


def start(stamp):
    try:
        threads = [logger, google_update, detector]
        if os.environ.get('local'):
            threads = [logger]
            Auth.dev.printer(f'Запуск бота локально за {time_now() - stamp} сек.')
        else:
            Auth.dev.start(stamp)
            Auth.dev.printer(f'Бот запущен за {time_now() - stamp} сек.')

        for thread_element in threads:
            _thread.start_new_thread(thread_element, ())
        executor.start_polling(dispatcher, allowed_updates=functions.allowed_updates)
    except IndexError and Exception:
        Auth.dev.thread_except()


if __name__ == '__main__' and os.environ.get('local'):
    start(stamp1)
