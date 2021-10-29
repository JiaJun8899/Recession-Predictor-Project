import os
import telebot
from telegramchart import *


#import TELEGRAM API KEY HERE
my_secret = '2018817369:AAE6G4FVD3qSwRonngAa7-wAX92bVpyKUec'
bot = telebot.TeleBot(my_secret)


# Get the directory where this script is running
script_dir = os.path.dirname(__file__)

# Get the datapng directory
datapng_dir = os.path.join(script_dir, '../../telegram_charts/')


#WELCOME MESSAGE
@bot.message_handler(commands=['start'])
def send_welcome(message):
        bot.reply_to(message, "welcome to 1002 Project Bot" + "\n"
  'For more info click /help.\n'
  )

##HELP COMMAND
@bot.message_handler(commands=['help'])
def help_command(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   keyboard.add(
       telebot.types.InlineKeyboardButton(
           "Visit our website", url="http://34.87.128.123/"
       )
   )
   bot.send_message(
       message.chat.id,
       '1) To receive a list of data that is available for download /info.\n',
       reply_markup=keyboard
   )
## GET INFO
@bot.message_handler(commands=['info'])
def get_info(message):
   keyboard = telebot.types.InlineKeyboardMarkup()
   bot.send_message(
       message.chat.id,
       'Choose the data you are interested in. \n'
       '1) To get CPI data /cpi.\n' +
       '2) To get Market Yield data /yield.\n' +
       '3) To get Industrial Production Ratedata /industrial.\n' +
       '4) To get Treasury Bill Rate data /bill.\n' +
       '5) To get Recession data /recession.\n' +
       '6) To get Capacity data /capacity.\n'
       '7) To get Unemployment data /unemployment.\n' ,
       reply_markup=keyboard
   )

##method to call for data
@bot.message_handler(commands=['cpi'])
def get_data(message):
  keyboard = telebot.types.InlineKeyboardMarkup()
  startyear = 2009
  j = 0
  for i in range(0, 4):
      keyboard.row(
        telebot.types.InlineKeyboardButton(str(startyear+i+j+1), callback_data='showchart01-cpi-' + str(startyear+i+j+1)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+2), callback_data='showchart01-cpi-' + str(startyear+i+j+2)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+3), callback_data='showchart01-cpi-' + str(startyear+i+j+3))
      )
      j += 2

  bot.send_message(
       message.chat.id,
       'Welcome to cpi data. Please choose the year to download. To go back to the main menu, /info',
       reply_markup=keyboard
   )

##method to call for data
@bot.message_handler(commands=['bill'])
def get_data(message):
  keyboard = telebot.types.InlineKeyboardMarkup()
  startyear = 2009
  j = 0
  for i in range(0, 4):
      keyboard.row(
        telebot.types.InlineKeyboardButton(str(startyear+i+j+1), callback_data='showchart01-treasurybill-' + str(startyear+i+j+1)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+2), callback_data='showchart01-treasurybill-' + str(startyear+i+j+2)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+3), callback_data='showchart01-treasurybill-' + str(startyear+i+j+3))
      )
      j += 2

  bot.send_message(
       message.chat.id,
       'Welcome to bill data. Please choose the year to download. To go back to the main menu, /info',
       reply_markup=keyboard
   )

##method to call for data
@bot.message_handler(commands=['industrial'])
def get_data(message):
  keyboard = telebot.types.InlineKeyboardMarkup()
  startyear = 2009
  j = 0
  for i in range(0, 4):
      keyboard.row(
        telebot.types.InlineKeyboardButton(str(startyear+i+j+1), callback_data='showchart01-industrial-' + str(startyear+i+j+1)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+2), callback_data='showchart01-industrial-' + str(startyear+i+j+2)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+3), callback_data='showchart01-industrial-' + str(startyear+i+j+3))
      )
      j += 2

  bot.send_message(
       message.chat.id,
       'Welcome to industrial data. Please choose the year to download. To go back to the main menu, /info',
       reply_markup=keyboard
   )

##method to call for data
@bot.message_handler(commands=['yield'])
def get_data(message):
  keyboard = telebot.types.InlineKeyboardMarkup()
  startyear = 2009
  j = 0
  for i in range(0, 4):
      keyboard.row(
        telebot.types.InlineKeyboardButton(str(startyear+i+j+1), callback_data='showchart01-yield-' + str(startyear+i+j+1)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+2), callback_data='showchart01-yield-' + str(startyear+i+j+2)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+3), callback_data='showchart01-yield-' + str(startyear+i+j+3))
      )
      j += 2

  bot.send_message(
       message.chat.id,
       'Welcome to yield data. Please choose the year to download. To go back to the main menu, /info',
       reply_markup=keyboard
   )

##method to call for data
@bot.message_handler(commands=['recession'])
def get_data(message):
  keyboard = telebot.types.InlineKeyboardMarkup()
  startyear = 2009
  j = 0
  for i in range(0, 4):
      keyboard.row(
        telebot.types.InlineKeyboardButton(str(startyear+i+j+1), callback_data='showchart01-rec-' + str(startyear+i+j+1)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+2), callback_data='showchart01-rec-' + str(startyear+i+j+2)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+3), callback_data='showchart01-rec-' + str(startyear+i+j+3))
      )
      j += 2

  bot.send_message(
       message.chat.id,
       'Welcome to recession data. Please choose the year to download. To go back to the main menu, /info',
       reply_markup=keyboard
   )

##method to call for data
@bot.message_handler(commands=['capacity'])
def get_data(message):
  keyboard = telebot.types.InlineKeyboardMarkup()
  startyear = 2009
  j = 0
  for i in range(0, 4):
      keyboard.row(
        telebot.types.InlineKeyboardButton(str(startyear+i+j+1), callback_data='showchart01-capacity-' + str(startyear+i+j+1)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+2), callback_data='showchart01-capacity-' + str(startyear+i+j+2)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+3), callback_data='showchart01-capacity-' + str(startyear+i+j+3))
      )
      j += 2

  bot.send_message(
       message.chat.id,
       'Welcome to unemployment data. Please choose the year to download. To go back to the main menu, /info',
       reply_markup=keyboard
   )

##method to call for data
@bot.message_handler(commands=['unemployment'])
def get_data(message):
  keyboard = telebot.types.InlineKeyboardMarkup()
  startyear = 2009
  j = 0
  for i in range(0, 4):
      keyboard.row(
        telebot.types.InlineKeyboardButton(str(startyear+i+j+1), callback_data='showchart01-employ-' + str(startyear+i+j+1)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+2), callback_data='showchart01-employ-' + str(startyear+i+j+2)),
        telebot.types.InlineKeyboardButton(str(startyear+i+j+3), callback_data='showchart01-employ-' + str(startyear+i+j+3))
      )
      j += 2

  bot.send_message(
       message.chat.id,
       'Welcome to unemployment data. Please choose the year to download. To go back to the main menu, /info',
       reply_markup=keyboard
   )

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    calldata = call.data
    if calldata.startswith('showchart01'):
        callback_datatype = calldata.split('-')[1]
        getstartyear = calldata.split('-')[2]
        getendyear = int(getstartyear) + 1
        bot.send_message(chat_id=call.message.chat.id,text=str(getstartyear) + " --- " + str(getendyear))
        telegramchart(callback_datatype, str(getstartyear) + '-01-01', str(getendyear) + '-01-01')
        photo = open(datapng_dir + callback_datatype + '.png', 'rb')
        bot.send_photo(call.message.chat.id, photo)
        bot.send_message(chat_id=call.message.chat.id,text=str('Go back to main menu: /info'))

bot.polling()
