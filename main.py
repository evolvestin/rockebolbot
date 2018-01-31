# 462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4
import telebot

token = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"

bot = telebot.TeleBot(token)
bot.config['api_key'] = "462725941:AAFxYxX0G_smCog6ZS-f2T_vqVfdUwCTRH4"
bot.send_message(396978030, "test")
upd = bot.get_updates()
print(upd)
# message_from_user = last_upd.message
# print(message_from_user)
import logging

logger = telebot.logger
telebot.logger.setLevel(logging.DEBUG)
