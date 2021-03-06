#!/usr/bin/python3
# -*- coding: utf-8 -*-
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from datetime import datetime
import logging, sys, json

#Import the answers dict from databases/answers.py
sys.path.insert(0, '../databases/')
from answers import answers

home_dir = '../'#Bot's home loction.
log_location =  home_dir+'logs/bot.log'#Loction of log file.
logging.basicConfig(filename=log_location ,format='%(asctime)s - %(name)s - %(message)s', level=logging.INFO)

#Read Bot's token from file.
TOKEN_location = home_dir+"bot/TOKEN.txt"
TOKEN_file = open(TOKEN_location, 'r')
TOKEN = TOKEN_file.read()[:-1]#For \n end of file :]
TOKEN_file.close()

admins = ['554868848']

updater = Updater(token=TOKEN)

class User:
    def __init__(self):
        self.id = None
        self.chat = None
        self.fname = None
        self.lname = None
        self.uname = None

user = User()

# Start function for answering /start command.
def start(bot, update, args):
    if len(args) > 0:#Check if start has any arguments
        message = " ".join(args)
        if message=='help':
            answer = answers['help_pv']
        else:
            answer = answers['start']
    else:
        answer = answers['start']
    message_id = update.message.message_id
    user.chat = update.message.chat_id #Get chat ID.
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)#Send answer message to chat ID.

# Help function for answering /help command
def help(bot, update):
    user.chat = update.message.chat_id
    user.id = update.message.from_user.id
    if user.chat == user.id:#If user send message as private message
        answer = answers['help_pv']
    else:
        answer = answers['help_pub']
    message_id = update.message.message_id
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# ask function for answering /ask command
def ask(bot, update):
    if 'reply_to_message' in str(update.message):#Check if message is as reply message!
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['ask']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# bitcoin function for answering /bitcoin command
def bitcoin(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['bitcoin']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# botinfo function for answering /botinfo command
def botinfo(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['botinfo']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# farsi function for answering /farsi command
def farsi(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['farsi']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# flood function for answering /flood command
def flood(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['flood']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# free function for answering /free command
def free(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['free']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# grub function for answering /grub command
def grub(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['grub']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# hacker function for answering /hacker command
def hacker(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['hacker']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# kali function for answering /kali command
def kali(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['kali']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# lamp function for answering /lamp command
def lamp(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['lamp']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# link function for answering /link command
def link(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['link']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# mahak function for answering /mahak command
def mahak(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['mahak']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

#Report message to admin
def report(bot, update):
    chat_id = update.message.chat_id
    report_id = update.message.message_id
    if 'reply_to_message' in str(update.message):
        message = eval(str(update.message.reply_to_message))#Convert reply_message information to dict; TODO: Make it easier.
        #Get the message informations
        message_epoch = int(message["date"])#Get message epoch time (timestramp)
        message_date = datetime.fromtimestamp(message_epoch)#Convert to real date
        message_text = message["text"]
        user.chat = chat_id
        user.id = message["from"]["id"]
        user.fname = message["from"]["first_name"]
        user.lname = message["from"]["last_name"]
        user.uname = message["from"]["username"]
        #Report text
        report = "#Report\nmessage:\n{0}\n\nGroupID:\n\
{1}\nUserID:\n{2}\nName:\n{3} {4}\nusername:\n\
@{5}\nDate:\n{6}".format(message_text, user.chat, user.id, user.fname, user.lname, user.uname, message_date)
        for admin in admins:#Send report to each admin
            bot.send_message(chat_id=admin, text=report)
    #Delete reporter message
    bot.delete_message(chat_id=chat_id, message_id=report_id)
        

# searx function for answering /searx command
def searx(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['searx']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# smart function for answering /smart command
def smart(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['smart']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# tor function for answering /tor command
def tor(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['tor']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

# xampp function for answering /xampp command
def xampp(bot, update):
    if 'reply_to_message' in str(update.message):
        message_id = update.message.reply_to_message.message_id
    else:
        message_id = update.message.message_id
    user.chat = update.message.chat_id
    answer = answers['xampp']
    bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id, parse_mode=ParseMode.MARKDOWN)

#Read user messages
def messages(bot, update):
    user.chat = update.message.chat_id
    message = str(update.message.text).encode('utf-8').decode('utf-8')
    answer = str()
    ubuntus = ['اوبنتو', 'ابنتو', 'ابونتو']
    works = {'کار کرده؟', 'بلده؟'}
    for ubuntu in ubuntus:
        if ubuntu in message:#Check if user say ubuntu as wrong!
            answer = answer + " *اوبونتو\n"
            break
    for work in works:
        if work in message:#Ask your question at first!
            answer = answer + " بهتر است به جای ارسال مطلب خود در چندین پیام، همه‌ی متن را در یک پیام نوشته و ارسال کنید.\n"
            break
    if len(answer) > 0:#has bot any answer?!
        message_id = update.message.message_id
        bot.send_message(chat_id=user.chat, text=answer, reply_to_message_id=message_id)


dispatcher = updater.dispatcher

start_command = CommandHandler('start', start, pass_args=True)
dispatcher.add_handler(start_command) #Add /start command handler.

help_command = CommandHandler('help', help)
dispatcher.add_handler(help_command) #Add /help command handler.

ask_command = CommandHandler('ask', ask)
dispatcher.add_handler(ask_command) #Add /ask command handler.

bitcoin_command = CommandHandler('bitcoin', bitcoin)
dispatcher.add_handler(bitcoin_command) #Add /bitcoin command handler.


botinfo_command = CommandHandler('botinfo', botinfo)
dispatcher.add_handler(botinfo_command) #Add /botinfo command handler.

farsi_command = CommandHandler('farsi', farsi)
dispatcher.add_handler(farsi_command) #Add /farsi command handler.


flood_command = CommandHandler('flood', flood)
dispatcher.add_handler(flood_command) #Add /flood command handler.


free_command = CommandHandler('free', free)
dispatcher.add_handler(free_command) #Add /free command handler.


grub_command = CommandHandler('grub', grub)
dispatcher.add_handler(grub_command) #Add /grub command handler.


hacker_command = CommandHandler('hacker', hacker)
dispatcher.add_handler(hacker_command) #Add /hacker command handler.


kali_command = CommandHandler('kali', kali)
dispatcher.add_handler(kali_command) #Add /kali command handler.


lamp_command = CommandHandler('lamp', lamp)
dispatcher.add_handler(lamp_command) #Add /lamp command handler.


link_command = CommandHandler('link', link)
dispatcher.add_handler(link_command) #Add /link command handler.


mahak_command = CommandHandler('mahak', mahak)
dispatcher.add_handler(mahak_command) #Add /mahak command handler.

report_command = CommandHandler('report', report)
dispatcher.add_handler(report_command) #Add /report command handler.

searx_command = CommandHandler('searx', searx)
dispatcher.add_handler(searx_command) #Add /searx command handler.


smart_command = CommandHandler('smart', smart)
dispatcher.add_handler(smart_command) #Add /smart command handler.


tor_command = CommandHandler('tor', tor)
dispatcher.add_handler(tor_command) #Add /tor command handler.

xampp_command = CommandHandler('xampp', xampp)
dispatcher.add_handler(xampp_command) #Add /xampp command handler.

message_handler = MessageHandler(Filters.text, messages)
dispatcher.add_handler(message_handler) #Add message handler.


print("READY!")

#Start polling
updater.start_polling()
updater.idle()
