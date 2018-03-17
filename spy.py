# -*- coding: utf-8 -*-
#equip

import telebot
from telebot import types
import urllib3
import requests
import time
from time import sleep
import datetime
from datetime import datetime
import _thread

#=================================================================
token = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"
bot = telebot.TeleBot(token)

clkwait = 61
coltwink = 23
globtime = 0
beatva = 0
timefort = 0

less = '🌲'
morfort = '⚓️'
gori = '⛰'
mo = '🇲🇴'
gp = '🇬🇵'
cy = '🇨🇾'
va = '🇻🇦'
im = '🇮🇲'
eu = '🇪🇺'
ki = '🇰🇮'
atk = '⚔️'
deff = '🛡'
eq = '🎽'

idMe = 396978030
idBlack = 394850016
idDBlack = 200299701 #MISSSPACEX
idBlue = 491625180
idDYellow = 485591553
idWhite = 430602902
idRed = 519673442 #DARETEN
idRed2 = 200299701 #MISSSPACEX
idDRed = 497892874
idTwilight = 462139760 #NAMI_LEE
idDTwilight = 350037139

idChatPeregovorka = -1001175146945
idChatCommandirka = -1001116128920

urlClear = 'http://bitlux.ru/evolve.php?text=none'
urldo = 'http://bitlux.ru/evolve.php?text='
urlcoldonate = 'http://bitlux.ru/donate.php?donate='
urleq = 'http://bitlux.ru/equip.html'
urleqlog = 'http://bitlux.ru/equip.php?eq='
#====================================================================================
starttime = int(datetime.utcfromtimestamp(int(int(datetime.now().timestamp()) + 3 * 60 * 60)).strftime('%H'))
if starttime == 16 or starttime == 17 or starttime == 18 or starttime == 19:
    keyboardst = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboardst.row(less + 'Лес', mo, eq + 'Экипировка')
    keyboardst.row(gp, cy, va)
    keyboardst.row(im, eu, ki)
    keyboardst.row(less + 'Лесной форт', gori + 'Горный форт', morfort + 'Морской форт')
else:
    keyboardst = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboardst.row(less + 'Лес', mo, eq + 'Экипировка')
    keyboardst.row(gp, cy, va)
    keyboardst.row(im, eu, ki)
bot.send_message(idMe, "<i>._.</i>", reply_markup=keyboardst, parse_mode='HTML')


def prikaz():
    time.sleep(clkwait)
    content = requests.get(urlClear)
    bot.send_message(idMe, '<i>Исполнено</i>', reply_markup=keyboard, parse_mode='HTML')


@bot.message_handler(commands=['time'])
def handle_chas_command(message):
    global globtime
    global beatva
    global timefort
    if beatva == 'da':
        bot.send_message(message.chat.id, '<b>БИТВА СКОРО!</b>\nСмотрите, время тикает: ' + globtime, parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, 'Время: ' + str(globtime))


@bot.message_handler(commands=['id'])
def handle_id_command(message):
    orbo = message.chat.id
    if orbo > 0:
        bot.send_message(message.chat.id, "Твой ID: " + str(orbo))
    elif orbo < 0:
        bot.send_message(message.chat.id, "ID этой группы: " + str(orbo))


@bot.callback_query_handler(func=lambda call: True)
def callback_equip(call):
    global clkwait
    global keyboard
    global zader
    if call.message.chat.id == idMe:
        if call.data == 'attack':
            bot.edit_message_text(chat_id=call.message.chat.id, text=atk + 'Шмот надеваем <code>(' + str(zader) + ')</code>', message_id=call.message.message_id, parse_mode='HTML')
            content = requests.get(urldo + 'Attack')
            prikaz()
            content = requests.get(urleqlog + 'Attack')
        elif call.data == 'defend':
            bot.edit_message_text(chat_id=call.message.chat.id, text=deff + 'Шмот надеваем <code>(' + str(zader) + ')</code>', message_id=call.message.message_id, parse_mode='HTML')
            content = requests.get(urldo + 'Defend')
            prikaz()
            content = requests.get(urleqlog + 'Defend')


@bot.message_handler(func=lambda message: message.text)
def repeat_all_messages(message):
    global globtime
    global clkwait
    global zader
    global keyboard
    global timefort
    if message.forward_date is not None:
        origmes = message.forward_date
        origmesH = datetime.utcfromtimestamp(int(origmes + 3 * 60 * 60)).strftime('%H')
        origmesM = datetime.utcfromtimestamp(int(origmes)).strftime('%M')
        origmesS = datetime.utcfromtimestamp(int(origmes)).strftime('%S')
        origtime = ' <code> ' + str(origmesH) + ':' + str(origmesM) + ':' + str(origmesS) + '[F]</code>'
    else:
        origtime = ' <code> ' + str(globtime) + '</code>'

    specmessage = '<code>: </code>' + message.text + origtime

    if timefort == 0:
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row(less + 'Лес', mo, eq + 'Экипировка')
        keyboard.row(gp, cy, va)
        keyboard.row(im, eu, ki)
    else:
        keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        keyboard.row(less + 'Лес', mo, eq + 'Экипировка')
        keyboard.row(gp, cy, va)
        keyboard.row(im, eu, ki)
        keyboard.row(less + 'Лесной форт', gori + 'Горный форт', morfort + 'Морской форт')

    if message.chat.id == idDBlack and message.forward_date is not None:
        if str(message.forward_from.username) == 'CWRedBot':
            bot.send_message(idChatCommandirka, atk + im + specmessage, parse_mode='HTML')
        elif str(message.forward_from.username) == 'ToweRobot':
            bot.send_message(idChatCommandirka, deff + gp + specmessage, parse_mode='HTML')

    elif message.chat.id == idRed:
        bot.send_message(idChatCommandirka, atk + im + '<code>(Dareten)</code>' + specmessage, parse_mode='HTML')

    elif message.chat.id == idDRed:
        bot.send_message(idChatCommandirka, deff + im + specmessage, parse_mode='HTML')

    elif message.chat.id == idBlack:
        bot.send_message(idChatCommandirka, atk + gp + specmessage, parse_mode='HTML')

    elif message.chat.id == idBlue:
        bot.send_message(idChatCommandirka, atk + eu + specmessage, parse_mode='HTML')

    elif message.chat.id == idDYellow:
        bot.send_message(idChatCommandirka, deff + va + specmessage, parse_mode='HTML')

    elif message.chat.id == idWhite:
        bot.send_message(idChatCommandirka, atk + cy + specmessage, parse_mode='HTML')

    elif message.chat.id == idDTwilight:
        bot.send_message(idChatCommandirka, deff + ki + specmessage, parse_mode='HTML')

    elif message.chat.id == idTwilight:
        bot.send_message(idChatCommandirka, ki + specmessage, parse_mode='HTML')

    elif message.chat.id == idMe:
        if message.text == less + 'Лес':
            bot.send_message(idMe, 'Идем в' + less + 'Лес <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'les')
            prikaz()

        elif message.text == less + 'Лесной форт':
            bot.send_message(idMe, 'Идем в ' + less + 'Лесной форт <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'lesfort')
            prikaz()
        elif message.text == morfort + 'Морской форт':
            bot.send_message(idMe, 'Идем в ' + morfort + 'Морской форт <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'morfort')
            prikaz()
        elif message.text == gori + 'Горный форт':
            bot.send_message(idMe, 'Идем в ' + gori + 'Горный форт <code>(' + str(zader) + ')</code>', parse_mode='HTML')
            content = requests.get(urldo + 'gorifort')
            prikaz()

        elif str(message.text).startswith('/donate'):
            donate = message.text
            donate = donate.replace('/donate ', '')
            donateform = urlcoldonate + donate
            content = requests.get(urldo + 'donate')
            content = requests.get(donateform)
            donate = int(donate) * coltwink
            bot.send_message(idMe, 'Вдонатить ~' + str(donate) + ' <code> (' + str(zader) + ')</code>', parse_mode='HTML')
            prikaz()

        elif message.text == eq + 'Экипировка':
            equiplog = requests.get(urleq).text
            if equiplog == 'Attack':
                equiplog = atk + 'Атакерская'
            elif equiplog == 'Defend':
                equiplog = deff + 'Деферская'
            keyroad = types.InlineKeyboardMarkup(row_width=2)
            buttons = []
            buttons.append(types.InlineKeyboardButton(text=atk + 'Шмот', callback_data='attack'))
            buttons.append(types.InlineKeyboardButton(text=deff + 'Шмот', callback_data='defend'))
            keyroad.add(*buttons)
            bot.send_message(idMe, eq + 'Экипировка: ' + equiplog, reply_markup=keyroad, parse_mode='HTML')

        elif message.text == mo or message.text == gp or message.text == cy or message.text == va or message.text == im or message.text == eu or message.text == ki:
            bot.send_message(idMe, 'Идем в ' + message.text + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
            if message.text == mo:
                content = requests.get(urldo + 'mo')
            elif message.text == gp:
                content = requests.get(urldo + 'gp')
            elif message.text == cy:
                content = requests.get(urldo + 'cy')
            elif message.text == va:
                content = requests.get(urldo + 'va')
            elif message.text == im:
                content = requests.get(urldo + 'im')
            elif message.text == eu:
                content = requests.get(urldo + 'eu')
            elif message.text == ki:
                content = requests.get(urldo + 'ki')
            prikaz()


def bitva_detector():
    global globtime
    global clkwait
    global hours
    global minutes
    global curr_time
    global zader
    global beatva
    while True:
        try:
            sleep(0.3)
            curr_time = int(datetime.now().timestamp())
            hourso = datetime.utcfromtimestamp(int(curr_time + 3 * 60 * 60)).strftime('%H')
            minuteso = datetime.utcfromtimestamp(int(curr_time)).strftime('%M')
            secondso = datetime.utcfromtimestamp(int(curr_time)).strftime('%S')
            hours = int(datetime.utcfromtimestamp(int(curr_time + 3 * 60 * 60)).strftime('%H'))
            minutes = int(datetime.utcfromtimestamp(int(curr_time)).strftime('%M'))
            seconds = int(datetime.utcfromtimestamp(int(curr_time)).strftime('%S'))
            globtime = str(hourso) + ':' + str(minuteso) + ':' + str(secondso)
            if hours == 3 or hours == 7 or hours == 11 or hours == 15 or hours == 19 or hours == 23:
                if minutes < 30:
                    clkwait = 30 + 1 # плюс доп задержка
                    beatva = 'net'
                elif minutes > 30 and minutes < 50:
                    beatva = 'da'
                    clkwait = 15 + 1 # плюс доп задержка
                elif minutes > 50 and minutes < 58:
                    beatva = 'da'
                    clkwait = 8 + 1 # плюс доп задержка
                elif minutes > 58 and minutes < 59:
                    beatva = 'da'
                    clkwait = 1 + 1 # плюс доп задержка
                elif minutes > 59 and seconds > 0:
                    clkwait = 1 + 1 # плюс доп задержка
                    if seconds > 40:
                        clkwait = 0.3 + 0.1 # плюс доп задержка
            else:
                clkwait = 60 + 1 # плюс задержка
                beatva = 'net'

            zader = clkwait - 1
        except Exception as e:
            sleep(0.3)


def merc_detector():
    global hours
    global minutes
    global curr_time
    global keyboard
    while True:
        try:
            sleep(1)
            merc_sec = int(datetime.utcfromtimestamp(int(curr_time)).strftime('%S'))
            if hours == 3 or hours == 7 or hours == 11 or hours == 15 or hours == 19 or hours == 23:
                if merc_sec == 25 and minutes == 59:
                    bot.send_message(idChatCommandirka, "Woop-woop! That's the sound of da ebolbo-police!", parse_mode='HTML')
                elif merc_sec == 30 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 35 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 40 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 45 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 50 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
                elif merc_sec == 55 and minutes == 59:
                    bot.send_message(idChatCommandirka, '59:' + str(merc_sec), parse_mode='HTML')
            elif hours == 4 or hours == 8 or hours == 12 or hours == 16 or hours == 20 or hours == 24:
                if merc_sec == 0 and minutes == 0:
                    bot.send_message(idChatCommandirka, '00:00', parse_mode='HTML')
                elif merc_sec == 3 and minutes == 0:
                    bot.send_message(idChatCommandirka, '<i>Опасность миновала. Можете продолжать ничего не делать.</i>', parse_mode='HTML')
        except Exception as e:
            sleep(1)


def fort_detector():
    global timefort
    global hours
    while True:
        try:
            sleep(60)
            if hours == 16 or hours == 17 or hours == 18 or hours == 19:
                timefort = 1
            else:
                timefort = 0
        except Exception as e:
            sleep(60)

def telepol():
    try:
        bot.polling(none_stop=True, timeout=60)
    except:
        bot.stop_polling()
        sleep(5)
        telepol()

if __name__ == '__main__':
    _thread.start_new_thread(bitva_detector, ())
    _thread.start_new_thread(fort_detector, ())
    _thread.start_new_thread(merc_detector, ())
    telepol()
