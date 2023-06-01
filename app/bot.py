from telebot import TeleBot

bot = TeleBot(token='')

user_id = 0

def send(msg):
    bot.send_message(user_id,msg)