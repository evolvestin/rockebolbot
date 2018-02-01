#url = "https://api.telegram.org/bot462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4/"
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
token = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"
bot = telebot.TeleBot(token)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли, в принципе
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.polling(none_stop=True)
