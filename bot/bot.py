#!/usr/bin/python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
from datetime import datetime
import logging

home_dir = '../'#Bot's home loction.
log_location =  home_dir+'logs/bot.log'#Loction of log file.
logging.basicConfig(filename=log_location ,format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)

#Read Bot's token from file.
TOKEN_location = home_dir+"bot/TOKEN.txt"
TOKEN_file = open(TOKEN_location, 'r')
TOKEN = TOKEN_file.read()[:-1]#For \n end of file :]
TOKEN_file.close()

updater = Updater(token=TOKEN)


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

# Start function for answering /start command.
def start(bot, update):
    user.chat = update.message.chat_id #Get chat ID.
    answer = answers['start']
    bot.send_message(chat_id=user.chat, text=answer)#Send answer message to chat ID.

# Help function for answering /help command
def help(bot, update):
    user.chat = update.message.chat_id #Get chat ID.
    answer = answers['help']
    bot.send_message(chat_id=user.chat, text=answer)#Send answer message to chat ID.

dispatcher = updater.dispatcher

start_command = CommandHandler('start', start)
dispatcher.add_handler(start_command) #Add /start command handler.

help_command = CommandHandler('help', help)
dispatcher.add_handler(help_command) #Add /help command handler.

print("READY!")

#Start polling
updater.start_polling()
updater.idle()