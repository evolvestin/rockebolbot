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

url = 'http://bitlux.ru/evolve.php?text=pep'
url2 = 'http://bitlux.ru/evolve.php?text=pep2'
url3 = 'http://bitlux.ru/evolve.php?text=les'
url4 = 'http://bitlux.ru/evolve.php?text=mo'
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
        content = requests.get(url2)
    elif message.chat.id == idDYellow:
        bot.send_message(idChatCommandirka, "<code>деф 🇻🇦: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idWhite:
        bot.send_message(idChatPeregovorka, "<code>🇨🇾: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idDRed:
        bot.send_message(idChatPeregovorka, "<code>деф 🇮🇲: " + message.text + "</code>", parse_mode='HTML')
    elif message.chat.id == idDTwilight:
        bot.send_message(idChatPeregovorka, "<code>деф 🇰🇮: " + message.text + "</code>", parse_mode='HTML')
    elif message.text == '🌲Лес':
        bot.send_message(idMe, "иди в лес")
        content = requests.get(url3)
        time.sleep(1)
        content = requests.get(url)
    elif message.text == mo:
        bot.send_message(idMe, "<code>Деф "+ mo + "</code>", parse_mode='HTML')
        content = requests.get(url4)
        time.sleep(1)
        content = requests.get(url)




if __name__ == '__main__':
     bot.polling(none_stop=True)
