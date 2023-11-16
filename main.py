import os

import telebot
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text='Чаво надо??')

@bot.message_handler(content_types=['text'])
def answer(message):
    answer = message.text
    bot.send_message(message.chat.id, text=answer)



def main():
    while True:
        bot.polling(none_stop=True)


if __name__ == '__main__':
    main()
