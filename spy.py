# -*- coding: utf-8 -*-

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import telebot
from telebot import types
import urllib3
import re
import requests
import time
from time import sleep
import datetime
from datetime import datetime
import _thread
import random

# ======================================================================================================================
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds1 = ServiceAccountCredentials.from_json_keyfile_name('worker1.json', scope)
creds2 = ServiceAccountCredentials.from_json_keyfile_name('worker2.json', scope)
client1 = gspread.authorize(creds1)
client2 = gspread.authorize(creds2)
sheet1 = client1.open('chats').sheet1
sheet2 = client2.open('chats').sheet1
listsheet1 = client1.open('list').sheet1
listsheet2 = client2.open('list').sheet1
try:
    chats1 = sheet1.col_values(1)
    chats2 = sheet2.col_values(2)
    list1 = listsheet1.col_values(1)
    list2 = listsheet1.col_values(2)
    list3 = listsheet2.col_values(3)
    list4 = listsheet2.col_values(4)
except:
    chats1 = 0
    chats2 = 0
    list1 = 0
    list2 = 0
    list3 = 0
    list4 = 0
tkn = chats1[0]
bot = telebot.TeleBot(tkn)

less = '🌲'
gori = '⛰'
gold = '💰'

atk = '⚔️'
deff = '🛡'
mo = '🇲🇴'
gp = '🇬🇵'
cy = '🇨🇾'
va = '🇻🇦'
im = '🇮🇲'
eu = '🇪🇺'
ki = '🇰🇮'
skal = '🖤'
bats = '🦇'
turt = '🐢'
oplt = '☘️'
rose = '🌹'
farm = '🍆'
ambr = '🍁'

plus = 3  # часовой пояс
retro = int(chats2[0])
split_bots = ''
split_spec = ''
split_version = ''
global_split = ['', '', '', '', 0]

idMe = 396978030

idChatDevelopment = -1001309670055
idChannelPins = -1001218234200

srch_towers = '(' + skal + '|' + bats + '|' + turt + '|' + oplt + '|' + rose + '|' + farm + '|' + ambr + ')'
srch_retrotowers = '(' + mo + '|' + gp + '|' + im + '|' + cy + '|' + va + '|' + eu + '|' + ki + ')'

chat_ids = [int(chats1[1]), int(chats1[2]), int(chats1[3]), int(chats1[4]), int(chats1[5]), int(chats1[6])]
chat_names = [chats2[1], chats2[2], chats2[3], chats2[4], chats2[5], chats2[6]]
idChatPinsUnion = chat_ids[0]
idChatPinsEnemy = chat_ids[1]
idChatDetector = chat_ids[2]
idChatRetroPinsUnion = chat_ids[3]
idChatRetroPinsEnemy = chat_ids[4]
idChatRetroDetector = chat_ids[5]

fraze25 = ['...', '-cCc-', '..', '.', '....', 'сСс..']

spycorp_ids = []
for new in list1:
    spycorp_ids.append(int(new))
spycorp_spec = list2
spycorp_tower = list3
spycorp_version = list4

a_union = [ambr, oplt, skal]
a_towers = [skal, bats, turt, oplt, rose, farm, ambr]
a_retrounion = [mo, gp, va, eu]
a_retrotowers = [mo, gp, cy, va, im, eu, ki]


NBOT = 'C' + 'h' + 'a' + 't' + 'W' + 'a' + 'r' + 's' + 'B' + 'o' + 't'
# ======================================================================================================================
bot.send_message(idMe, '🤤')


def spadder(key):
    if key == 1:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button = []
        button.append(types.InlineKeyboardButton(text='CW1', callback_data='CW1'))
        button.append(types.InlineKeyboardButton(text='CW3', callback_data='CW3'))
        button.append(types.InlineKeyboardButton(text='⚡️Сплит', callback_data='Split'))
        button.append(types.InlineKeyboardButton(text='🙄Отмена', callback_data='brake_ext'))
        button.append(types.InlineKeyboardButton(text='😈Отвергнуть', callback_data='brake'))
        keyboard.add(*button)
    elif key == 2:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button = []
        button.append(types.InlineKeyboardButton(text='Все', callback_data='all_cw1'))
        button.append(types.InlineKeyboardButton(text=atk, callback_data='atk_cw1'))
        button.append(types.InlineKeyboardButton(text=deff, callback_data='deff_cw1'))
        button.append(types.InlineKeyboardButton(text='⚰️Отмена', callback_data='otmena'))
        keyboard.add(*button)
    elif key == 3:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button = []
        button.append(types.InlineKeyboardButton(text='Все', callback_data='all_cw3'))
        button.append(types.InlineKeyboardButton(text=atk, callback_data='atk_cw3'))
        button.append(types.InlineKeyboardButton(text=deff, callback_data='deff_cw3'))
        button.append(types.InlineKeyboardButton(text='⚰️Отмена', callback_data='otmena'))
        keyboard.add(*button)

    elif key == 4:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button = []
        button.append(types.InlineKeyboardButton(text=mo, callback_data=mo))
        button.append(types.InlineKeyboardButton(text=gp, callback_data=gp))
        button.append(types.InlineKeyboardButton(text=cy, callback_data=cy))
        button.append(types.InlineKeyboardButton(text=va, callback_data=va))
        button.append(types.InlineKeyboardButton(text=im, callback_data=im))
        button.append(types.InlineKeyboardButton(text=eu, callback_data=eu))
        button.append(types.InlineKeyboardButton(text=ki, callback_data=ki))
        button.append(types.InlineKeyboardButton(text='⚰️Отмена', callback_data='otmena'))
        keyboard.add(*button)
    elif key == 5:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button = []
        button.append(types.InlineKeyboardButton(text=skal, callback_data=skal))
        button.append(types.InlineKeyboardButton(text=bats, callback_data=bats))
        button.append(types.InlineKeyboardButton(text=turt, callback_data=turt))
        button.append(types.InlineKeyboardButton(text=oplt, callback_data=oplt))
        button.append(types.InlineKeyboardButton(text=rose, callback_data=rose))
        button.append(types.InlineKeyboardButton(text=farm, callback_data=farm))
        button.append(types.InlineKeyboardButton(text=ambr, callback_data=ambr))
        button.append(types.InlineKeyboardButton(text='⚰️Отмена', callback_data='otmena'))
        keyboard.add(*button)
    elif key == 6:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button = []
        button.append(types.InlineKeyboardButton(text='👌Добавить', callback_data='good'))
        button.append(types.InlineKeyboardButton(text='⚰️Отмена', callback_data='otmena'))
        keyboard.add(*button)
    elif key == 7:
        keyboard = types.InlineKeyboardMarkup(row_width=3)
        button = []
        button.append(types.InlineKeyboardButton(text='👌Добавить', callback_data='good'))
        button.append(types.InlineKeyboardButton(text='⚰️Отмена', callback_data='otmena'))
        keyboard.add(*button)
    elif key == 8:
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        button = []
        button.append(types.InlineKeyboardButton(text='Ввести ботов', callback_data='split_bots'))
        button.append(types.InlineKeyboardButton(text='Ввести специализацию + замок', callback_data='split_spec'))
        button.append(types.InlineKeyboardButton(text='Ввести маркировку CW', callback_data='split_version'))
        button.append(types.InlineKeyboardButton(text='⚰️Отмена', callback_data='otmena'))
        keyboard.add(*button)
    return keyboard


def rawtime(stamp):
    rtime = []
    weekday = datetime.utcfromtimestamp(int(stamp + plus * 60 * 60)).strftime('%a')
    if weekday == 'Mon':
        weekday = 'Пн'
    elif weekday == 'Tue':
        weekday = 'Вт'
    elif weekday == 'Wed':
        weekday = 'Ср'
    elif weekday == 'Thu':
        weekday = 'Чт'
    elif weekday == 'Fri':
        weekday = 'Пт'
    elif weekday == 'Sat':
        weekday = 'Сб'
    elif weekday == 'Sun':
        weekday = 'Вс'
    day = datetime.utcfromtimestamp(int(stamp + plus * 60 * 60)).strftime('%d')
    month = datetime.utcfromtimestamp(int(stamp + plus * 60 * 60)).strftime('%m')
    year = datetime.utcfromtimestamp(int(stamp + plus * 60 * 60)).strftime('%Y')
    hours = datetime.utcfromtimestamp(int(stamp + plus * 60 * 60)).strftime('%H')
    minutes = datetime.utcfromtimestamp(int(stamp)).strftime('%M')
    seconds = datetime.utcfromtimestamp(int(stamp)).strftime('%S')
    rtime.append(weekday)
    rtime.append(day)
    rtime.append(month)
    rtime.append(year)
    rtime.append(hours)
    rtime.append(minutes)
    rtime.append(seconds)
    return rtime


def rawtime_lite(stamp):
    rtime = []
    hours = datetime.utcfromtimestamp(int(stamp + plus * 60 * 60)).strftime('%H')
    minutes = datetime.utcfromtimestamp(int(stamp)).strftime('%M')
    seconds = datetime.utcfromtimestamp(int(stamp)).strftime('%S')
    rtime.append(hours)
    rtime.append(minutes)
    rtime.append(seconds)
    return rtime


def edit_chats(key, id):
    global idChatPinsUnion
    global idChatPinsEnemy
    global idChatDetector
    global idChatRetroPinsUnion
    global idChatRetroPinsEnemy
    global idChatRetroDetector
    global chat_ids
    global client1
    me = 1
    if key == 0:
        idChatPinsUnion = id
    elif key == 1:
        idChatPinsEnemy = id
    elif key == 2:
        idChatDetector = id
    elif key == 3:
        idChatRetroPinsUnion = id
    elif key == 4:
        idChatRetroPinsEnemy = id
    elif key == 5:
        idChatRetroDetector = id
    else:
        me = 0
    if me == 1:
        try:
            sheet1 = client1.open('chats').sheet1
        except:
            creds1 = ServiceAccountCredentials.from_json_keyfile_name('worker1.json', scope)
            client1 = gspread.authorize(creds1)
            sheet1 = client1.open('chats').sheet1
        sheet1.update_cell(key + 2, 1, id)
    chat_ids[key] = id
    return me


@bot.message_handler(commands=['time'])
def handle_time_command(message):
    time = rawtime(int(datetime.now().timestamp()))
    text = 'Время: ' + str(time[4]) + ':' + str(time[5]) + ':' + str(time[6]) + \
        ' <code>(' + str(time[0]) + ' ' + str(time[1] + '.' + str(time[2]) + '.' + \
        str(time[3])) + ', GMT+' + str(plus) + ')</code>'
    bot.send_message(message.chat.id, text, parse_mode='HTML')


@bot.message_handler(commands=['id'])
def handle_id_command(message):
    if message.reply_to_message is None:
        text = 'Твой ID: <code>' + str(message.from_user.id) + '</code>\n'
        if message.chat.id < 0:
            text = text + 'Group ID: <code>' + str(message.chat.id) + '</code>'
    elif message.reply_to_message:
        id = str(message.reply_to_message.from_user.id)
        if message.reply_to_message.from_user.username:
            username = '@' + str(message.reply_to_message.from_user.username)
        else:
            username = ''
        if message.reply_to_message.from_user.first_name:
            firstname = str(message.reply_to_message.from_user.first_name)
        else:
            firstname = ''
        if message.reply_to_message.from_user.last_name:
            lastname = str(message.reply_to_message.from_user.last_name)
        else:
            lastname = ''

        signature = str(message.reply_to_message.from_user.is_bot)
        isbot = 'Тип: '
        if signature == 'True' and username == '@rockebolbot':
            isbot = isbot + '<b>Ето я</b>🖤'
        elif signature == 'True':
            isbot = isbot + '<b>Бот</b>'
        elif signature == 'False':
            isbot = isbot + '<b>Человек</b>'
        else:
            isbot = ''

        text = firstname + ' ' + lastname + ' [<b>' + username + '</b>]\n' + \
            'ID: <code>' + id + '</code>\n' + isbot

    bot.send_message(message.chat.id, text, parse_mode='HTML')


@bot.message_handler(commands=['status'])
def handle_status_command(message):
    if message.chat.id < 0:
        chatname = '???'
        chatpins = 'Нет'
        chatdetector = 'Нет'
        chatretropins = 'Нет'
        chatretrodetector = 'Нет'
        for i in chat_ids:
            if message.chat.id == i:
                chatname = chat_names[chat_ids.index(i)]
            if message.chat.id == idChatPinsUnion or message.chat.id == idChatPinsEnemy:
                chatpins = 'Да'
            if message.chat.id == idChatDetector:
                chatdetector = 'Да'
            if message.chat.id == idChatRetroPinsUnion or message.chat.id == idChatRetroPinsEnemy:
                chatretropins = 'Да'
            if message.chat.id == idChatRetroDetector:
                chatretrodetector = 'Да'
        if retro == 1:
            rstatus = 'Активен'
            retroUI = '       Ретро-пины  здесь: <b>' + chatretropins + '</b>\n' \
                      '       Ретро-детектор здесь: <b>' + chatretrodetector + '</b>\n'
        else:
            rstatus = 'Деактивирован'
            retroUI = ''

        text = 'Группа: ' + str(chatname) + ' (<code>' + str(message.chat.id) + '</code>)'

        if chatname != '???' or message.from_user.id == idMe:
            text = text + '\n' \
                'Пины приходят сюда: <b>' + chatpins + '</b>\n' + \
                'Детектор битвы здесь: <b>' + chatdetector + '</b>\n' + \
                'Ретро-режим: <b>' + rstatus + '</b>\n' + retroUI

        bot.send_message(message.chat.id, text, parse_mode='HTML')


@bot.message_handler(commands=['start'])
def handle_start_command(message):
    if message.chat.id > 0:
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        button = []
        button.append(types.InlineKeyboardButton(text='Я шпион🕵🏿', callback_data='Spy'))
        button.append(types.InlineKeyboardButton(text='Нет😡', callback_data='NoSpy'))
        spy = 0
        for i in spycorp_ids:
            if message.chat.id == i:
                spy = 1
        if spy == 1:
            text = 'Привет шпион\n' \
                   'Зачем жмякаешь /start? Впрочем, не важно. Думаю, ты продолжишь слать мне пины исправно🤤'
            button = []
        else:
            text = 'Привет. Не будем всё усложнять, ладно? Просто скажи, будешь ли ты для нас шпионом?'
        keyboard.add(*button)
        bot.send_message(message.chat.id, text, reply_markup=keyboard)


@bot.message_handler(commands=['berman'])
def handle_berman_command(message):
    if retro == 1:
        rsec = rawtime_lite(int(datetime.now().timestamp()))
        seconds = int(rsec[2])
        if seconds == 0 or seconds == 10 or seconds == 11 or seconds == 20 or seconds == 21 or seconds == 30 or seconds == 31 or seconds == 40 or seconds == 41 or seconds == 50 or seconds == 51:
            bot.send_message(message.chat.id, 'Только что в мире умер один человек, почтим его память тремя секундами перемирия')
            sleep(3)
            bot.send_message(message.chat.id, 'Траур завершен, у вас есть 7 секунд, чтобы успеть повоевать')
        else:
            bot.send_message(message.chat.id, 'Траур завершен, у вас есть ~7 секунд, чтобы успеть повоевать')


@bot.message_handler(commands=['beatva'])
def handle_beatvas_command(message):
    if retro == 1:
        bot.send_document(message.chat.id, 'CgADAgAD8wAD98PZSEpxdZ5jnUKlAg')


@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    global global_split
    global spycorp_ids
    global spycorp_spec
    global spycorp_tower
    global spycorp_version
    if call.message.chat.id > 0:
        if call.data == 'Spy':
            keyboard = spadder(1)
            if call.message.chat.username:
                username = ' @' + str(call.message.chat.username)
            else:
                username = ''
            if call.message.chat.first_name:
                firstname = str(call.message.chat.first_name) + ' '
            else:
                firstname = ''
            if call.message.chat.last_name:
                lastname = str(call.message.chat.last_name)
            else:
                lastname = ''
            devtext = str(call.message.chat.id) + '.   ' + firstname + lastname + username
            text = 'А ты мне нравишься😍\nДанные твои я отправил моему Повелителю, подожди, никуда не уходи.'

            bot.send_message(idChatDevelopment, devtext, reply_markup=keyboard)
            bot.edit_message_text(chat_id=call.message.chat.id, text=text, message_id=call.message.message_id)
        elif call.data == 'NoSpy':
            text = 'Пидора ответ😡 Ну и зачем ты зашел сюда? Я шпион-бот, ' \
                   'больше ничо не умею...\nНу может и умею, но тебе не расскажу точно, бака😑\n\n' \
                   'Если вдруг, ты захочешь нам пошпионить всё-таки, то прожми /start и выбери другой стул.'

            bot.edit_message_text(chat_id=call.message.chat.id, text=text, message_id=call.message.message_id)
    if call.message.chat.id < 0:
        if call.message.chat.id == idChatDevelopment:
            if call.data == 'brake':
                text = '<b>Повелитель</b> посчитал вас недостойным права быть шпионом. You have been banned forever.'
                search = re.search('(\d+)\.', call.message.text)
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + '\n🤤Отвергнут', message_id=call.message.message_id)
                try:
                    bot.send_message(search.group(1), text, parse_mode='HTML')
                except:
                    bot.send_message(call.message.chat.id, 'Сообщение об отмене доставить не удалось😤')
            elif call.data == 'brake_ext':
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + '\n🙄Отменен',
                                      message_id=call.message.message_id)
            elif call.data == 'CW1':
                keyboard = spadder(2)
                text = '\n------\nТип: ' + call.data
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'CW3':
                keyboard = spadder(3)
                text = '\n------\nТип: ' + call.data
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'Split':
                keyboard = spadder(8)
                global_split[0] = call.message.text + '\n------\nТип: ' + 'Сплит'
                bot.edit_message_text(chat_id=call.message.chat.id, text=global_split[0],
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'otmena':
                keyboard = spadder(1)
                search = re.search('(.*)(\n------\n)(.*)', call.message.text)
                text = search.group(1)
                global_split = ['', '', '', '', 0]
                bot.edit_message_text(chat_id=call.message.chat.id, text=text,
                                      reply_markup=keyboard, message_id=call.message.message_id)

            elif call.data == 'all_cw1':
                keyboard = spadder(4)
                text = '\nСпециализация: ' + 'Все'
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'atk_cw1':
                keyboard = spadder(4)
                text = '\nСпециализация: ' + atk
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'deff_cw1':
                keyboard = spadder(4)
                text = '\nСпециализация: ' + deff
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'all_cw3':
                keyboard = spadder(5)
                text = '\nСпециализация: ' + 'Все'
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'atk_cw3':
                keyboard = spadder(5)
                text = '\nСпециализация: ' + atk
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == 'deff_cw3':
                keyboard = spadder(5)
                text = '\nСпециализация: ' + deff
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == mo or call.data == gp or call.data == cy or \
                 call.data == va or call.data == im or call.data == eu or call.data == ki:
                keyboard = spadder(6)
                text = '\nЗамок: ' + call.data
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)
            elif call.data == skal or call.data == bats or call.data == turt or \
                call.data == oplt or call.data == rose or call.data == farm or call.data == ambr:
                keyboard = spadder(6)
                text = '\nЗамок: ' + call.data
                bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                      reply_markup=keyboard, message_id=call.message.message_id)

            elif call.data == 'split_bots':
                text = 'Ввести юзернеймы ботов, разделяя запятыми каждый из Сплита'
                global_split[4] = 1
                bot.send_message(call.message.chat.id, text)
            elif call.data == 'split_spec':
                text = 'Ввести специализации и замок, разделяя запятыми каждый из Сплита' + \
                    '\nСпециализации: ' + atk + deff + '\nЗамки:\n' + \
                    skal + bats + turt + oplt + rose + farm + ambr + '\n' + \
                    mo + gp + cy + va + im + eu + ki + '\n\nНапример:' + atk + mo + '.' + farm
                global_split[4] = 2
                bot.send_message(call.message.chat.id, text)
            elif call.data == 'split_version':
                text = 'Ввести маркировку CW (CW1 = 1, CW3 = 3), разделяя запятыми каждый из Сплита\n' + \
                    'Например: 1.3'
                global_split[4] = 3
                bot.send_message(call.message.chat.id, text)
            elif call.data == 'good':
                global spycorp_ids
                global spycorp_spec
                global spycorp_tower
                global spycorp_version
                key = 0
                idsearch = re.search('(\d+)\.', call.message.text)
                typesearch = re.search('\n------\nТип: (.*)\n', call.message.text)
                specsearch = re.search('\nСпециализация: (.*)', call.message.text)
                towersearch = re.search('\nЗамок: (.*)', call.message.text)

                if specsearch.group(1) == atk:
                    spec = 'atk'
                elif specsearch.group(1) == deff:
                    spec = 'deff'
                elif specsearch.group(1) == 'Все':
                    spec = '_'
                else:
                    spec = specsearch.group(1)

                if typesearch.group(1) == 'CW1':
                    version = 1
                elif typesearch.group(1) == 'CW3':
                    version = 3
                elif typesearch.group(1) == 'Сплит':
                    versearch = re.search('\nМаркировка: (.*)', call.message.text)
                    version = versearch.group(1)

                for i in spycorp_ids:
                    if int(idsearch.group(1)) == i:
                        key = 1
                if key != 1:
                    global client1
                    togoogle = [str(idsearch.group(1)), spec, towersearch.group(1), version]
                    spycorp_ids.append(int(idsearch.group(1)))
                    spycorp_spec.append(spec)
                    spycorp_tower.append(towersearch.group(1))
                    spycorp_version.append(version)
                    try:
                        listsheet1 = client1.open('list').sheet1
                    except:
                        creds1 = ServiceAccountCredentials.from_json_keyfile_name('worker1.json', scope)
                        client1 = gspread.authorize(creds1)
                        listsheet1 = client1.open('list').sheet1
                    listsheet1.insert_row(togoogle, 1)

                    worktext = '😈Хе-хе! <b>Повелителю</b> ты понравился. Теперь ты принят на работу. ' \
                               'Так что, начиная с этого момента, всё, что ты сюда пришлешь, ' \
                               'будет отправлено в нужные <i>места</i>.\n\n' \
                               '<b>ВАЖНО!</b> Пусть мы и дали тебе удобную клавиатуру для отправки пина, ' \
                               'старайся использовать именно <b>форвард</b> приказа, так ты повышаешь шансы понять ' \
                               'ситуацию и принять верное решение.' \

                    text = '\nСтатус: 🎽Принят на работу'
                    bot.edit_message_text(chat_id=call.message.chat.id, text=call.message.text + text,
                                          message_id=call.message.message_id)
                    try:
                        bot.send_message(int(idsearch.group(1)), worktext, parse_mode='HTML')
                    except:
                        bot.send_message(call.message.chat.id, 'Сообщение c поздравлениями доставить не удалось😱')
                else:
                    text = 'Человек с таким id уже есть в системе, если нужно, используй:\n' \
                           '/del_' + str(idsearch.group(1)) + '\n' \
                           'Это удалит его из системы и ты сможешь нажать кнопку повторно.'
                    bot.send_message(call.message.chat.id, text)


@bot.message_handler(content_types=["new_chat_members"])
def get_new_member(message):
    if message.chat.title:
        title = str(message.chat.title) + ' ('
    else:
        title = ' ('
    user_id = str(message.from_user.id)
    chat_id = str(message.chat.id)
    if message.from_user.username:
        chat_user = '@' + str(message.from_user.username) + ' / '
    else:
        if message.from_user.first_name:
            firstname = str(message.from_user.first_name)
        else:
            firstname = ''
        if message.from_user.last_name:
            lastname = str(message.from_user.last_name) + ' '
        else:
            lastname = ''
        chat_user = firstname + ' ' + lastname

    if message.new_chat_member is not None and message.new_chat_member.username == 'rockebolbot':
        bot.send_message(idChatDevelopment,
                         chat_user + user_id + ': Добавил бота в чат: ' + title + chat_id + ')')


@bot.message_handler(content_types=['audio', 'video', 'document', 'location', 'contact', 'sticker', 'voice'])
def redmessages(message):
    if message.from_user.id != 205356091 \
            and message.from_user.id != 105907720 \
            and message.from_user.id != 280993442 \
            and message.from_user.id != idMe:
        temp = rawtime_lite(int(datetime.now().timestamp()))
        hour = int(temp[0])
        min = int(temp[1])
        if hour == 0 or hour == 8 or hour == 16:
            if min > 54:
                bot.delete_message(message.chat.id, message.message_id)
        if retro == 1:
            if hour == 3 or hour == 7 or hour == 11 or hour == 15 or hour == 19 or hour == 23:
                if min > 54:
                    bot.delete_message(message.chat.id, message.message_id)

    elif message.chat.id == idMe:
        if message.document:
            bot.send_message(message.chat.id, 'file_id: ' + str(message.document.file_id))
        if message.voice:
            bot.send_message(message.chat.id, 'file_id: ' + str(message.voice.file_id))


@bot.message_handler(func=lambda message: message.text)
def repeat_all_messages(message):
    global global_split
    if message.chat.id > 0:
        if message.forward_date is not None:
            ftime = ''
            adder = '  '
            forwarded = message.forward_date
            stamp = int(datetime.now().timestamp())
            forwardedD = datetime.utcfromtimestamp(int(forwarded + plus * 60 * 60)).strftime('%d')
            currentday = datetime.utcfromtimestamp(int(stamp + plus * 60 * 60)).strftime('%d')
            time = rawtime_lite(forwarded)
            if currentday != forwardedD:
                time_all = rawtime(forwarded)
                ftime = '\n<code>' + str(time_all[0]) + ' ' + str(time_all[1] + '.' + \
                    str(time_all[2]) + '.' + str(time_all[3])) + '</code>  '
            if str(message.forward_from.username) == NBOT or \
                    str(message.forward_from.username) == 'ChatWarsClassicBot':
                temp = forwardCW(message)
                text = temp[0]
                adder = temp[1]
            else:
                text = pin_analizer(message)
            messagetime = adder + ftime + '<code>' + str(time[0]) + ':' + str(time[1]) + ':' + str(time[2]) + '[F]</code>'
        else:
            text = pin_analizer(message)
            time = rawtime_lite(int(datetime.now().timestamp()))
            messagetime = ' <code> ' + str(time[0]) + ':' + str(time[1]) + ':' + str(time[2]) + '</code>'
        specmessage = '<code>: </code>' + text + messagetime

        for i in spycorp_ids:
            if message.chat.id == i:
                spec_inarray = spycorp_spec[spycorp_ids.index(i)]
                tower = spycorp_tower[spycorp_ids.index(i)]
                version = str(spycorp_version[spycorp_ids.index(i)])
                if spec_inarray == '_':
                    spec = ''
                elif spec_inarray == 'atk':
                    spec = atk
                elif spec_inarray == 'def':
                    spec = deff
                else:
                    spec_grand = spec_inarray.split('.')
                    tower_grand = tower.split('.')
                    version_grand = version.split('.')
                    tower = tower_grand[0]
                    version = version_grand[0]
                    if message.forward_from:
                        for z in spec_grand:
                            if str(message.forward_from.username) == z:
                                tower = tower_grand[spec_grand.index(z)]
                                version = version_grand[spec_grand.index(z)]
                    search = re.search(srch_towers, tower)
                    retrosearch = re.search(srch_retrotowers, tower)
                    if search:
                        spec = tower.replace(search.group(1), '')
                        tower = search.group(1)
                    elif retrosearch:
                        spec = tower.replace(retrosearch.group(1), '')
                        tower = retrosearch.group(1)

                if version == '3':
                    adress = idChatPinsEnemy
                    for v in a_union:
                        if tower == v:
                            adress = idChatPinsUnion
                elif version == '1':
                    adress = idChatRetroPinsEnemy
                    for v in a_retrounion:
                        if tower == v:
                            adress = idChatRetroPinsUnion
                else:
                    adress = idChatPinsUnion

                bot.send_message(adress, spec + tower + specmessage, parse_mode='HTML')
                bot.send_message(idChannelPins, spec + tower + specmessage, parse_mode='HTML')
    else:
        if message.from_user.id == idMe:
            good = '✅Исполнено'
            bad = 'Что-то пошло не так'
            if str(message.text).startswith('/chat'):
                try:
                    key = int(message.text.replace('/chat ', ''))
                except:
                    key = 10
                edit = edit_chats(key, message.chat.id)
                if edit == 1:
                    bot.send_message(message.chat.id, good)
                else:
                    bot.send_message(message.chat.id, bad)
            if str(message.text).startswith('/name'):
                global chat_names
                try:
                    name = message.text.replace('/name ', '')
                except:
                    name = 10
                if name != 10:
                    global sheet1
                    try:
                        google = sheet1.col_values(1)
                    except:
                        creds1 = ServiceAccountCredentials.from_json_keyfile_name('worker1.json', scope)
                        client1 = gspread.authorize(creds1)
                        sheet1 = client1.open('chats').sheet1
                        google = sheet1.col_values(1)
                    for g in google:
                        if str(message.chat.id) == g:
                            sheet1.update_cell(google.index(g) + 1, 2, str(name))

                    for i in chat_ids:
                        if message.chat.id == i:
                            chat_names[chat_ids.index(i)] = name
                    bot.send_message(message.chat.id, good)
                else:
                    bot.send_message(message.chat.id, bad)

        if message.chat.id == idChatDetector or message.chat.id == idChatRetroDetector:
            chat = message.chat.id
            if message.from_user.id == idMe and message.reply_to_message:
                    if message.text == 'не пиши' or message.text == 'пидорас' or message.text == 'говно':
                        bot.send_voice(chat, 'AwADAgADXAEAAu7TEEiU1v4upM88swI',
                                       reply_to_message_id=message.reply_to_message.message_id)
                    elif message.text == 'пин':
                        try:
                            bot.pin_chat_message(message.chat.id, message.reply_to_message.message_id)
                        except:
                            try:
                                bot.send_message(message.from_user.id, 'Я не админ в чате, чтобы пинить, учти это')
                            except:
                                temp = 0

            elif message.from_user.id != 205356091 \
                    and message.from_user.id != 105907720 \
                    and message.from_user.id != 280993442 \
                    and message.from_user.id != idMe:
                temp = rawtime_lite(int(datetime.now().timestamp()))
                hour = int(temp[0])
                min = int(temp[1])
                if hour == 0 or hour == 8 or hour == 16:
                    if min > 54:
                        bot.delete_message(message.chat.id, message.message_id)
                if retro == 1:
                    if hour == 3 or hour == 7 or hour == 11 or hour == 15 or hour == 19 or hour == 23:
                        if min > 54:
                            bot.delete_message(message.chat.id, message.message_id)
        elif message.chat.id == idChatDevelopment:
            if global_split[4] == 1:
                keyboard = spadder(8)
                if global_split[1] == '':
                    global_split[0] = global_split[0] + '\nСпециализация: ' + message.text
                    global_split[1] = message.text
                temp = bot.send_message(message.chat.id, global_split[0], reply_markup=keyboard)
            elif global_split[4] == 2:
                keyboard = spadder(8)
                if global_split[2] == '':
                    global_split[0] = global_split[0] + '\nЗамок: ' + message.text
                    global_split[2] = message.text
                temp = bot.send_message(message.chat.id, global_split[0], reply_markup=keyboard)
            elif global_split[4] == 3:
                keyboard = spadder(8)
                if global_split[3] == '':
                    global_split[0] = global_split[0] + '\nМаркировка: ' + message.text
                    global_split[3] = message.text
                temp = bot.send_message(message.chat.id, global_split[0], reply_markup=keyboard)

            if global_split[0] != '' and global_split[1] != '' and global_split[2] != '' and global_split[3] != '':
                keyboard = spadder(7)
                bot.edit_message_text(chat_id=temp.chat.id, text=temp.text,
                                      reply_markup=keyboard, message_id=temp.message_id)
            global_split[4] = 0

            if str(message.text).startswith('/add'):
                keyboard = spadder(1)
                try:
                    add = message.text.replace('/add_', '')
                    search = re.search('(\w+)', add)
                    text = str(search.group(1)) + '.'
                    bot.send_message(message.chat.id, text, reply_markup=keyboard)
                except:
                    text = 'Введен не верный id'
                    bot.send_message(message.chat.id, text)
            elif str(message.text).startswith('/del'):
                global listsheet1
                delete = message.text.replace('/del_', '')
                search = re.search('(\w+)', delete)
                marker = 0
                try:
                    google = listsheet1.col_values(1)
                except:
                    creds1 = ServiceAccountCredentials.from_json_keyfile_name('worker1.json', scope)
                    client1 = gspread.authorize(creds1)
                    listsheet1 = client1.open('list').sheet1
                    google = listsheet1.col_values(1)
                for m in google:
                    if str(search.group(1)) == m:
                        listsheet1.delete_row(google.index(m) + 1)
                        marker = 1

                for i in spycorp_ids:
                    if int(search.group(1)) == i:
                        spycorp_spec.pop(spycorp_ids.index(i))
                        spycorp_tower.pop(spycorp_ids.index(i))
                        spycorp_version.pop(spycorp_ids.index(i))
                        spycorp_ids.pop(spycorp_ids.index(i))
                        marker = 1
                if marker != 0:
                    text = '✅Человек удален из моих списков'
                else:
                    text = '❓Что-то пошло не так, не могу удалить человека из своих списков или его там и не было'
                bot.send_message(message.chat.id, text)


def pin_analizer(message):
    search = re.search(srch_towers, message.text)
    retro_search = re.search(srch_retrotowers, message.text)
    text = message.text
    if search:
        deepsearch = re.search('( )', message.text)
        if deepsearch:
            text = message.text.replace(deepsearch.group(1), '')
        deepsearch2 = re.search('(\n)', text)
        if deepsearch2:
            text = text.replace(deepsearch2.group(1), '  ')
    else:
        if retro_search:
            text = retro_search.group(1)
    return text


def forwardCW(message):
    if str(message.forward_from.username) == 'ChatWarsClassicBot':
        repsearch = re.search(srch_retrotowers + '(.+)' + atk + ':', message.text)
        kazsearch = re.search(srch_retrotowers + '(.+)( замок)', message.text)
        CWtime = message.forward_date
        CWtimeH = int(datetime.utcfromtimestamp(int(CWtime + plus * 60 * 60)).strftime('%H'))
        if repsearch:
            report = message.text.replace(repsearch.group(2), '')
            if CWtimeH > -1 and CWtimeH < 4:
                repchas = '0 часов'
            if CWtimeH > 3 and CWtimeH < 8:
                repchas = '4 часа'
            if CWtimeH > 7 and CWtimeH < 12:
                repchas = '8 часов'
            if CWtimeH > 11 and CWtimeH < 16:
                repchas = '12 часов'
            if CWtimeH > 15 and CWtimeH < 20:
                repchas = '16 часов'
            if CWtimeH > 19 and CWtimeH < 24:
                repchas = '20 часов'
            time = '\n<code>Битва в ' + str(repchas) + '.</code> '
            report = [report, time]
        elif kazsearch:
            kazflag = kazsearch.group(1)
            kazname = kazsearch.group(2)
            kazsearch = re.search('(Казна замка:\n)([0-9]+)' + gold + ' ([0-9]+)' + less + ' ([0-9]+)' + gori, message.text)
            if kazsearch:
                report = kazflag + kazname + ':' + '\n' + kazsearch.group(2) + gold + \
                         ' ' + kazsearch.group(3) + less + ' ' + kazsearch.group(4) + gori
                report = [report, '\n']
        else:
            report = ['Форварды из ЧВ отключены (кроме репортов и казны), ради вашей безопасности🌝', '']
        return report
    elif str(message.forward_from.username) == NBOT:
        text = srch_towers + '(.+) .+:.+ ' + deff + ':.+ Lvl: .+\nТвои результаты в бою:\n.+'
        repsearch = re.search(text, message.text)
        CWtime = message.forward_date
        CWtimeH = int(datetime.utcfromtimestamp(int(CWtime + plus * 60 * 60)).strftime('%H'))
        if repsearch:
            report = message.text.replace(repsearch.group(2), 'Солдат')
            if CWtimeH > 0 and CWtimeH <= 9:
                repchas = '01 час'
            if CWtimeH > 8 and CWtimeH < 17:
                repchas = '09 часов'
            if CWtimeH > 16 and CWtimeH < 25:
                repchas = '17 часов'
            time = '\n<code>Битва в ' + str(repchas) + '.</code> '
            report = [report, time]
        else:
            report = ['Форварды из ЧВ отключены (кроме репортов), ради вашей безопасности🌚', '']
        return report


def detector():
    while True:
        try:
            sleep(0.9)
            temp = rawtime_lite(int(datetime.now().timestamp()))
            hour = int(temp[0])
            min = int(temp[1])
            sec = int(temp[2])
            if hour == 7 or hour == 11 or hour == 15 or hour == 19 or hour == 23:
                if retro == 1:
                    if sec == 25 and min == 59:
                        rnd = random.randint(0, len(fraze25) - 1)
                        bot.send_message(idChatRetroDetector, fraze25[rnd], parse_mode='HTML')
                    elif sec == 30 and min == 59:
                        bot.send_message(idChatRetroDetector, '59:' + str(sec), parse_mode='HTML')
                        bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                    elif sec == 35 and min == 59:
                        bot.send_message(idChatRetroDetector, '59:' + str(sec), parse_mode='HTML')
                        bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                    elif sec == 40 and min == 59:
                        bot.send_message(idChatRetroDetector, '59:' + str(sec), parse_mode='HTML')
                        bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                    elif sec == 45 and min == 59:
                        bot.send_message(idChatRetroDetector, '59:' + str(sec), parse_mode='HTML')
                        bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                    elif sec == 50 and min == 59:
                        bot.send_message(idChatRetroDetector, '59:' + str(sec), parse_mode='HTML')
                        bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                    elif sec == 55 and min == 59:
                        bot.send_message(idChatRetroDetector, '59:' + str(sec), parse_mode='HTML')
                        bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
            elif hour == 0 or hour == 8 or hour == 16:
                if sec >= 0 and min == 0 and retro == 1:
                    bot.send_message(idChatRetroDetector, '00:0' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '00:0' + str(sec), parse_mode='HTML')
                    sleep(60)
                elif sec == 25 and min == 59:
                    rnd = random.randint(0, len(fraze25) - 1)
                    bot.send_message(idChatDetector, fraze25[rnd], parse_mode='HTML')
                elif sec == 30 and min == 59:
                    bot.send_message(idChatDetector, '59:' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                elif sec == 35 and min == 59:
                    bot.send_message(idChatDetector, '59:' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                elif sec == 40 and min == 59:
                    bot.send_message(idChatDetector, '59:' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                elif sec == 45 and min == 59:
                    bot.send_message(idChatDetector, '59:' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                elif sec == 50 and min == 59:
                    bot.send_message(idChatDetector, '59:' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
                elif sec == 55 and min == 59:
                    bot.send_message(idChatDetector, '59:' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '59:' + str(sec), parse_mode='HTML')
            elif hour == 12 or hour == 20:
                if sec >= 0 and min == 0 and retro == 1:
                    bot.send_message(idChatRetroDetector, '00:0' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '00:0' + str(sec), parse_mode='HTML')
                    sleep(60)
            elif hour == 1 or hour == 9 or hour == 17:
                if sec >= 0 and min == 0:
                    bot.send_message(idChatDetector, '00:0' + str(sec), parse_mode='HTML')
                    bot.send_message(idChannelPins, '00:0' + str(sec), parse_mode='HTML')
                    sleep(60)
        except Exception as e:
            sleep(0.9)


def telepol():
    try:
        bot.polling(none_stop=True, timeout=60)
    except:
        bot.stop_polling()
        sleep(0.5)
        telepol()


if __name__ == '__main__':
    _thread.start_new_thread(detector, ())
    telepol()
