#url = "https://api.telegram.org/bot462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4/"
#!/usr/bin/env python
#chat_id evo = 396978030
#chat_id ow = 394850016
#chat_id be = 491625180
#chat_id so = 485591553
#chat_id fb = 430602902
#chat_id gt = 497892874
#chat_id sm = 350037139
# -*- coding: utf-8 -*-

import telebot
import urllib3
token = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    #bot.send_message(396978030, message.text)

    if message.chat.id == 491625180: #be
        bot.send_message(-1001116128920, "🇪🇺: " + message.text)
    elif message.chat.id == 394850016: #ow
        bot.send_message(-1001175146945, "🇬🇵: " + message.text)
    elif message.chat.id == 485591553: #so
        bot.send_message(-1001116128920, "деф 🇻🇦: " + message.text)
    elif message.chat.id == 430602902: #fb
        bot.send_message(-1001175146945, "🇨🇾: " + message.text)
    elif message.chat.id == 497892874: #gt
        bot.send_message(-1001175146945, "деф 🇮🇲: " + message.text)
    elif message.chat.id == 350037139: #sm
        bot.send_message(-1001175146945, "деф 🇰🇮: " + message.text)
    elif message.chat.id == 396978030: #kke
        bot.send_message(396978030, "дебил: " + message.text)
    elif message.chat.id == 396978030:
        content = urllib.request.urlopen('http://bitlux.ru/evolve.php?text=les').read()

if __name__ == '__main__':
     bot.polling(none_stop=True)
