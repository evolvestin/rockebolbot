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

#globtime = ''
clkwait = 61

less = '🌲'
mo = '🇲🇴'
gp = '🇬🇵'
cy = '🇨🇾'
va = '🇻🇦'
im = '🇮🇲'
eu = '🇪🇺'
ki = '🇰🇮'
atk = '⚔️'
deff = '🛡'

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
urlles = 'http://bitlux.ru/evolve.php?text=les'
urlmo = 'http://bitlux.ru/evolve.php?text=mo'
urlgp = 'http://bitlux.ru/evolve.php?text=gp'
urlcy = 'http://bitlux.ru/evolve.php?text=cy'
urlva = 'http://bitlux.ru/evolve.php?text=va'
urlim = 'http://bitlux.ru/evolve.php?text=im'
urleu = 'http://bitlux.ru/evolve.php?text=eu'
urlki = 'http://bitlux.ru/evolve.php?text=ki'
urldonate = 'http://bitlux.ru/evolve.php?text=donate'
urlEqAtk = 'http://bitlux.ru/evolve.php?text=Attack'
urlEqDef = 'http://bitlux.ru/evolve.php?text=Defend'
urlEqLogAtk = 'http://bitlux.ru/equip.php?eq=Attack'
urlEqLogDef = 'http://bitlux.ru/equip.php?eq=Defend'
urlcoldonate = 'http://bitlux.ru/donate.php?donate='
urlEqcheck = 'http://bitlux.ru/equip.html'
#====================================================================================

keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
keyboard.row(less + 'Лес', mo, atk + 'Шмот', deff + 'Шмот')
keyboard.row(gp, cy, va)
keyboard.row(im, eu, ki)
bot.send_message(idMe, "._.", reply_markup=keyboard)

globtime = 0
beatva = 0
@bot.message_handler(commands=['time'])
def handle_chas_command(message):  
    global globtime
    global beatva
    if message.chat.id == idChatPeregovorka and beatva == 'da':
        bot.send_message(message.chat.id, '<b>БИТВА СКОРО</b><code>! Смотрите время тикает: ' + globtime + '</code>', parse_mode='HTML')
    else:
        bot.send_message(message.chat.id, '<code>Время: ' + globtime + '</code>', parse_mode='HTML')


@bot.message_handler(commands=['id'])
def handle_id_command(message):  
    orbo = message.chat.id
    if orbo > 0:
        bot.send_message(message.chat.id, "Твой ID: " + str(orbo))
    elif orbo < 0:
        bot.send_message(message.chat.id, "ID этой группы: " + str(orbo))

@bot.message_handler(commands=['equip'])
def handle_start_px(message):
    equips = requests.get(urlEqcheck)
    equip = equips.text
    if message.chat.id == idMe and equip == 'Attack':
        bot.send_message(idMe, '<code>Атакерский</code>', parse_mode='HTML')
    elif message.chat.id == idMe and equip == 'Defend':
        bot.send_message(idMe, '<code>Деферский</code>', parse_mode='HTML')
    elif message.chat.id != idMe:
        bot.send_message(message.chat.id, '<code>А ты кто? Думаешь мы тут шутки шутим? А ну не трожь.</code>', parse_mode='HTML')

@bot.message_handler(func=lambda message: message.text) #content_types=["text"]
def repeat_all_messages(message):
    global globtime
    global clkwait
    global zader
    if message.chat.id == idDBlack and message.forward_date is not None:
        if str(message.forward_from.username) == "CWRedBot":
            bot.send_message(idChatCommandirka, atk + im + "<code>: " + message.text + "</code>", parse_mode='HTML')
            #bot.send_message(idChatPeregovorka, atk + im + "<code>: " + message.text + "</code>", parse_mode='HTML')
        elif str(message.forward_from.username) == "ToweRobot":
            bot.send_message(idChatCommandirka, deff + gp + "<code>: " + message.text + "</code>", parse_mode='HTML')
            #bot.send_message(idChatPeregovorka, deff + gp + "<code>: " + message.text + "</code>", parse_mode='HTML')

    elif message.chat.id == idRed:
        bot.send_message(idChatCommandirka, atk + im + "<code>(Dareten): " + message.text + "</code>", parse_mode='HTML')
        #bot.send_message(idChatPeregovorka, atk + im + "<code>(Dareten): " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idDRed:
        bot.send_message(idChatCommandirka, deff + im + "<code>: " + message.text + "</code>", parse_mode='HTML')
	#bot.send_message(idChatPeregovorka, deff + im + "<code>: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idBlack:
        bot.send_message(idChatCommandirka, atk + gp + '<code>: </code>' + message.text + ' <code> ' + globtime + '</code>', parse_mode='HTML')
	#bot.send_message(idChatPeregovorka, atk + gp + "<code>: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idBlue:
        bot.send_message(idChatCommandirka, atk + eu + "<code>: " + message.text + "</code>", parse_mode='HTML')
        #bot.send_message(idChatPeregovorka, atk + eu + "<code>: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idDYellow:
        bot.send_message(idChatCommandirka, deff + va + "<code>: " + message.text + "</code>", parse_mode='HTML')
	#bot.send_message(idChatPeregovorka, deff + va + "<code>: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idWhite:
        bot.send_message(idChatCommandirka, atk + cy + "<code>: " + message.text + "</code>", parse_mode='HTML')
	#bot.send_message(idChatPeregovorka, atk + cy + "<code>: " + message.text + "</code>", parse_mode='HTML')    
    elif message.chat.id == idDTwilight:
        bot.send_message(idChatCommandirka, deff + ki + "<code>: " + message.text + "</code>", parse_mode='HTML')
	#bot.send_message(idChatPeregovorka, deff + ki + "<code>: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idTwilight:
        bot.send_message(idChatCommandirka, ki + "<code>: " + message.text + "</code>", parse_mode='HTML')
        #bot.send_message(idChatPeregovorka, ki + "<code>: " + message.text + "</code>", parse_mode='HTML')

#less
    elif message.chat.id == idMe and message.text == less + 'Лес':
        bot.send_message(idMe, 'Идем в' + less + 'Лес <code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlles)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#EqAtk
    elif message.chat.id == idMe and message.text == atk + 'Шмот':
        bot.send_message(idMe, atk + 'Шмот надеваем <code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlEqAtk)
        time.sleep(clkwait)
        content = requests.get(urlEqLogAtk)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#EqDef
    elif message.chat.id == idMe and message.text == deff + 'Шмот':
        bot.send_message(idMe, deff + 'Шмот надеваем <code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlEqDef)
        time.sleep(clkwait)
        content = requests.get(urlEqLogDef)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#donate
    elif message.chat.id == idMe and str(message.text).startswith('/donate'):
        donate = message.text
        donate = donate.replace('/donate ', '')
        donateform = urlcoldonate + donate
        content = requests.get(urldonate)
        content = requests.get(donateform)
        donate = int(donate) * 18
        donate = str(donate)
        bot.send_message(idMe, 'Вдонатить ~' + donate + ' <code> (' + str(zader) + ')</code>', parse_mode='HTML')
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
    #mo
    elif message.chat.id == idMe and message.text == mo:
        bot.send_message(idMe, 'Деф ' + mo + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlmo)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#gp
    elif message.chat.id == idMe and message.text == gp:
        bot.send_message(idMe, 'Идем в ' + gp + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlgp)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#cy
    elif message.chat.id == idMe and message.text == cy:
        bot.send_message(idMe, 'Идем в ' + cy + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlcy)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#va
    elif message.chat.id == idMe and message.text == va:
        bot.send_message(idMe, 'Идем в ' + va + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlva)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#im
    elif message.chat.id == idMe and message.text == im:
        bot.send_message(idMe, 'Идем в ' + im + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlim)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#eu
    elif message.chat.id == idMe and message.text == eu:
        bot.send_message(idMe, 'Идем в ' + eu + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urleu)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')
#ki
    elif message.chat.id == idMe and message.text == ki:
        bot.send_message(idMe, 'Идем в ' + ki + '<code>(' + str(zader) + ')</code>', parse_mode='HTML')
        content = requests.get(urlki)
        time.sleep(clkwait)
        content = requests.get(urlClear)
        bot.send_message(idMe, '<i>Исполнено</i>', parse_mode='HTML')

def bitva_detector():
    global globtime
    global clkwait
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

def telepol():
    try:
        bot.polling(none_stop=True, timeout=60)
    except:
        bot.stop_polling()
        sleep(5)
        telepol()

if __name__ == '__main__':
    _thread.start_new_thread(bitva_detector, ())
    telepol() 
