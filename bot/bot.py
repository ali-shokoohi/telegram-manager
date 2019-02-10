#!/usr/bin/python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging

home_dir = '../'#Bot's home loction.
log_location =  home_dir+'logs/bot.log'#Loction of log file.
logging.basicConfig(filename=log_location ,format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)

#Bot token.
token = "777099556:AAGUJtwLihGVQk2aAt9TgeVEXPf4aCMAy-U"
updater = Updater(token=token)

#Read command answers from files.
texts_location = home_dir+'databases/answers.txt'
texts_file = open(texts_location, 'r')
texts = texts_file.read()
answers = eval(texts)
texts_file.close()

class User:
    def __init__(self):
        self.id = None
        self.chat = None
        self.fname = None
        self.lname = None
        self.uname = None

user = User()

# Start function for answer /start command.
def start(bot, update):
    user.chat = update.message.chat_id #Get chat ID.
    answer = answers['start']
    bot.send_message(chat_id=user.chat, text=answer)#Send text message to chat ID.


dispatcher = updater.dispatcher

start_command = CommandHandler('start', start)
dispatcher.add_handler(start_command) #Add command handler /start.

print("READY!")

#Start polling
updater.start_polling()
updater.idle()