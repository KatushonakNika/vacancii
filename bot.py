TOKEN = '5163490828:AAEuql1HLYYvnyHO_hvh9K7E6bNcq1EW-bI'

import telebot

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message): # Название функции не играет никакой роли
    bot.send_message(message.chat.id, message.text)

if __name__ == '__main__':
     bot.infinity_polling()