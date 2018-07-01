#!/usr/bin/python3
from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import RegexHandler
from sys import exc_info as error
from string import ascii_lowercase
from string import digits
from random import choice

token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

def start(bot, update):
  username = update.message.from_user.first_name
  update.message.reply_text(greeting(username), parse_mode='Markdown')
  message = genre_head()

  for genre in genres:
    message += genre_list(genre['name'], genre['id'])

  update.message.reply_text(message, parse_mode='Markdown')

def artist(bot, update):
  genre_id = update.message.text.replace('/dl_', '')

  for genre in genres:
    if genre['id'] == genre_id:
       message = artist_head(genre['name'])

  for artist in artists:
    message += artist_list(artist['id'], artist['name'], genre_id)

  message += artist_list_end()
  update.message.reply_text(message, parse_mode='Markdown')

def download(bot, update):
  file = update.message.text.replace('/dl_', '')
  update.message.reply_text(u'\U0001F3BC\nhttp://music.com/{}.mp3'.format(file),
                            parse_mode='Markdown')

try:
  updater = Updater(token)
  dp = updater.dispatcher

  dp.add_handler(RegexHandler('/start', start))
  dp.add_handler(RegexHandler('^(/dl_[\d]+)$', artist))
  dp.add_handler(RegexHandler('^(/dl_[\d]+[\w]+)$', download))
  dp.add_handler(MessageHandler(Filters.text, start))

  updater.start_polling()
except:
  print(error())
  updater.stop()

################################################################################
# Messeges
def greeting(first_name):
  return '*Hello and welcome, {}!*\n'.format(first_name)

def genre_head():
  return '*What your favorite genre?*\n'

def genre_list(genre_name, genre_id):
  return '\n{}*{}*\n[ Choose {} /dl_{} ]\n'.format(u'\U0001F3B6', genre_name,
                                                   u'\U0001F449', genre_id)

def artist_head(genre_name):
  return 'What artist in {}*{}* you are looking for?\n'.format(u'\U0001F3B6',
                                                               genre_name)

def artist_list(artist_id, artist_name, genre_id):
  return '\n{} *{}*\n[Press for download {} /dl_{}{}]\n'.format(u'\U0001F468',
                                                                artist_name,
                                                                u'\U0001F449',
                                                                genre_id,
                                                                artist_id)

def artist_list_end():
  return '\n\nIf you choose a wrong genre press {} /start'.format(u'\U0001F449')

################################################################################
# Fake data
def digit():
  return ''.join(choice(digits) for iter in range(4))

def char():
  return ''.join(choice(ascii_lowercase) for iter in range(4))

genres = [{'id':digit(), 'name':'Rock'},
          {'id':digit(), 'name':'Classic'},
          {'id':digit(), 'name':'Pop'},
          {'id':digit(), 'name':'Dance'}]

artists = [{'id':char(), 'name':'Led Zeppeling'},
           {'id':char(), 'name':'Johann Sebastian Bach'},
           {'id':char(), 'name':'Madonna'},
           {'id':char(), 'name':'Tiesto'}]
