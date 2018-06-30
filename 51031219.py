#!/usr/bin/python3
from telegram.ext import Updater, Filters
from telegram.ext import CommandHandler, CallbackQueryHandler, MessageHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import requests

def start(bot, update):
    update.message.reply_text('Hello! I can show an awesome images for you. Choose!',
                              reply_markup=main_keyboard())

def meow(bot, update):
    query = update.callback_query
    photo = requests.get('http://aws.random.cat/meow').json()
    bot.send_photo(caption="Meow! :)",
                   photo=photo['file'],
                   chat_id=query.message.chat_id,
                   message_id=query.message.message_id,
                   reply_markup=action_keyboard())

def wooff(bot, update):
    query = update.callback_query
    photo = requests.get('https://dog.ceo/api/breed/husky/images/random').json()
    bot.send_photo(caption="Bwoof! :)",
                   photo=photo['message'],
                   chat_id=query.message.chat_id,
                   message_id=query.message.message_id,
                   reply_markup=action_keyboard())

def like(bot, update):
    query = update.callback_query
    bot.send_message(text='{}Likewise!'.format(u'\U0001F60A'),
                     chat_id=query.message.chat_id,
                     reply_markup=main_keyboard())

def great(bot, update):
    query = update.callback_query
    bot.send_message(text='{}Great!'.format(u'\U0001F60B'),
                     chat_id=query.message.chat_id,
                     reply_markup=main_keyboard())

def main_keyboard():
    keyboard = [[InlineKeyboardButton("Get Meow", callback_data='meow`'),
                 InlineKeyboardButton("Get Wooff", callback_data='wooff')]]
    return InlineKeyboardMarkup(keyboard)

def action_keyboard():
    keyboard = [[InlineKeyboardButton("Like!", callback_data='like'),
                 InlineKeyboardButton("Great!", callback_data='great')]]
    return InlineKeyboardMarkup(keyboard)

updater = Updater('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(meow, pattern='meow'))
updater.dispatcher.add_handler(CallbackQueryHandler(wooff, pattern='wooff'))
updater.dispatcher.add_handler(CallbackQueryHandler(like, pattern='like'))
updater.dispatcher.add_handler(CallbackQueryHandler(great, pattern='great'))
updater.dispatcher.add_handler(MessageHandler(Filters.text | Filters.photo, start))

updater.start_polling()
