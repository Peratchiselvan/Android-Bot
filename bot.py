# -*- coding: utf-8 -*-

import os
import telegram
from telegram.error import NetworkError, Unauthorized
from time import sleep
from telegram.ext import CommandHandler, MessageHandler, Filters
from telegram.ext import Updater


myToken = os.environ['TELEGRAM_TOKEN']


# Add the commands and reply commands in the commandDict with the following format
# "command":"reply message" 
commandDict={
"rom":"This is an APP Development Group. Not ROM Development Group!"
}


def main():
    updater = Updater(token=myToken)
    dispatcher = updater.dispatcher
    warn_handler = CommandHandler('warn', warn, pass_args=True)
    msg_handler = MessageHandler(Filters.status_update.new_chat_members,msg)
    dispatcher.add_handler(msg_handler)
    dispatcher.add_handler(warn_handler)
    updater.start_polling()
    print("Started...")

def msg(bot, update):
	# Welcome the member with the greet message
    update.message.reply_text("Welcome to the Android App Development Group! Ask any questions ** *about App Development* ** in the group , and one of our members will try to help you :)")

def warn(bot, update, args):
    arg = args[0].lower()
    if(arg in commandDict):
        if(update.message.reply_to_message != None):  
            update.message.reply_to_message.reply_text(commandDict[arg])
        else:
            update.message.reply_text(commandDict[arg])

if __name__ == '__main__':
    main()
