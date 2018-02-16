# -*- coding: utf-8 -*-

import telebot
import urllib3
import requests
import time
from telebot import types

#=================================================================
token = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"
bot = telebot.TeleBot(token)

less = '🌲'
mo = '🇲🇴'
gp = '🇬🇵'
cy = '🇨🇾'
va = '🇻🇦'
im = '🇮🇲'
eu = '🇪🇺'
ki = '🇰🇮'

idMe = 396978030
idBlack = 394850016
idBlue = 491625180
idDYellow = 485591553
idWhite = 430602902
idRed = 519673442 #DARETEN
idDRed = 497892874
idDTwilight = 350037139

idChatPeregovorka = -1001175146945
idChatCommandirka = -1001116128920

urlclear = 'http://bitlux.ru/evolve.php?text=none'
urlles = 'http://bitlux.ru/evolve.php?text=les'
urlmo = 'http://bitlux.ru/evolve.php?text=mo'
urlgp = 'http://bitlux.ru/evolve.php?text=gp'
urlcy = 'http://bitlux.ru/evolve.php?text=cy'
urlva = 'http://bitlux.ru/evolve.php?text=va'
urlim = 'http://bitlux.ru/evolve.php?text=im'
urleu = 'http://bitlux.ru/evolve.php?text=eu'
urlki = 'http://bitlux.ru/evolve.php?text=ki'
#====================================================================================

keyboard = types.ReplyKeyboardMarkup(one_time_keyboard=False, resize_keyboard=True)
keyboard.row(less + 'Лес', mo)
keyboard.row(gp, cy, va)
keyboard.row(im, eu, ki)
bot.send_message(idMe, "Choose one letter:", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text) #content_types=["text"]
def repeat_all_messages(message):
    if message.chat.id == idBlue: 
        bot.send_message(idChatCommandirka, "<code>🇪🇺: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idRed:
        bot.send_message(idChatCommandirka, "<code>🇮🇲(Dareten): " + message.text + "</code>", parse_mode='HTML')
        bot.send_message(idChatPeregovorka, "<code>🇮🇲(Dareten): " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idBlack:
        bot.send_message(idChatPeregovorka, "<code>🇬🇵: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idDYellow:
        bot.send_message(idChatCommandirka, "<code>деф 🇻🇦: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idWhite:
        bot.send_message(idChatPeregovorka, "<code>🇨🇾: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idDRed:
        bot.send_message(idChatPeregovorka, "<code>деф 🇮🇲: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idDTwilight:
        bot.send_message(idChatPeregovorka, "<code>деф 🇰🇮: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idMe and message.text == '🌲Лес':
        bot.send_message(idMe, "<code>В " + less + "Лес </code>", parse_mode='HTML')
        content = requests.get(urlles)
        time.sleep(1)
        content = requests.get(urlclear)
#mo
    elif message.chat.id == idMe and message.text == mo:
        bot.send_message(idMe, "<code>Деф " + mo + "</code>", parse_mode='HTML')
        content = requests.get(urlmo)
        time.sleep(1)
        content = requests.get(urlclear)
#gp
    elif message.chat.id == idMe and message.text == gp:
        bot.send_message(idMe, "<code>Идем в " + gp + "</code>", parse_mode='HTML')
        content = requests.get(urlgp)
        time.sleep(1)
        content = requests.get(urlclear)
#cy
    elif message.chat.id == idMe and message.text == cy:
        bot.send_message(idMe, "<code>Идем в " + cy + "</code>", parse_mode='HTML')
        content = requests.get(urlcy)
        time.sleep(1)
        content = requests.get(urlclear)
#va
    elif message.chat.id == idMe and message.text == va:
        bot.send_message(idMe, "<code>Идем в " + va + "</code>", parse_mode='HTML')
        content = requests.get(urlva)
        time.sleep(1)
        content = requests.get(urlclear)
#im
    elif message.chat.id == idMe and message.text == im:
        bot.send_message(idMe, "<code>Идем в " + im + "</code>", parse_mode='HTML')
        content = requests.get(urlim)
        time.sleep(1)
        content = requests.get(urlclear)
#eu
    elif message.chat.id == idMe and message.text == eu:
        bot.send_message(idMe, "<code>Идем в " + eu + "</code>", parse_mode='HTML')
        content = requests.get(urleu)
        time.sleep(1)
        content = requests.get(urlclear)
#ki
    elif message.chat.id == idMe and message.text == ki:
        bot.send_message(idMe, "<code>Идем в " + ki + "</code>", parse_mode='HTML')
        content = requests.get(urlki)
        time.sleep(1)
        content = requests.get(urlclear)



if __name__ == '__main__':
     bot.polling(none_stop=True)
