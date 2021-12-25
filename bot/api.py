import os

import telebot

from bot.Bot import Bot

client = telebot.TeleBot(os.getenv("TOKEN"))


@client.message_handler(content_types=['text'])
def reverse_message(message):
    bot = Bot()
    answer = bot.reverse_message(message.text)
    client.send_message(message.from_user.id, answer)
