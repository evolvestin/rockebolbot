#url = "https://api.telegram.org/bot462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4/"
#!/usr/bin/env python
# chat_id evo = 396978030
#chat_id ow = 394850016
# -*- coding: utf-8 -*-

import telebot
token = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(396978030, message.text)
    if message.chat.id == 394850016:
        bot.send_message(396978030, "он пишет, но что ты не узнаешь")
    return

if __name__ == '__main__':
     bot.polling(none_stop=True)
