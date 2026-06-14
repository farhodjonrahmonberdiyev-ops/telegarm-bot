import telebot
import os

bot = telebot.TeleBot(os.environ.get("TOKEN"))

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Salom! Bot ishlayapti ✅")

@bot.message_handler(commands=['help'])
def help_cmd(message):
    bot.send_message(message.chat.id, "Yordam kerakmi? 🤝")

bot.infinity_polling()
