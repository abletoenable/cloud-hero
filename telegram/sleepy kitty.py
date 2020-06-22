#telegram-bot Sleepy-Kitty for Yandex.Cloud CloudFunction

import telebot
from telebot import types
import json

import random


# Telegram Access
token = "TELEGRAM_BOT_TOKEN"
bot = telebot.TeleBot(token, threaded=False)


# Cloud Function Handler
def handler(event,context):
    body = json.loads(event['body'])
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])


# Buttons
button_start = types.KeyboardButton(r'🐱' + " Хочу котиков ")
button_continue = types.KeyboardButton(r'😻' + " Хочу ещё котиков ")
button_stop = types.KeyboardButton(r'🤪' + " Спасибо. Хватит ")


# Keyboards
keyboard_start = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_start.add(button_start)
keyboard_continue = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True)
keyboard_continue.add(button_continue, button_stop)


# Start
@bot.message_handler(commands=['start'])
def start_helper(message):
    start_message = "Привет! Если тебе плохо, я покажу тебе котиков. А если хорошо, тоже покажу"
    bot.send_message(message.chat.id, start_message, reply_markup=keyboard_start)


# Send photo
@bot.message_handler(regexp="Хочу котиков")
def send_kitty(message):
    file = str(random.randint(1,10))+'.jpg'
    photo = 'BUCKET_URL' + file
    bot.send_photo(message.chat.id, photo, reply_markup=keyboard_continue)


# Continue
@bot.message_handler(regexp="Хочу ещё котиков")
def send_kitty(message):
    file = str(random.randint(1,10))+'.jpg'
    photo = 'BUCKET_URL' + file
    bot.send_photo(message.chat.id, photo, reply_markup=keyboard_continue)


# Stop
@bot.message_handler(regexp="Спасибо. Хватит")
def goodby(message):
    end_message = 'Пока! До скорого!'
    bot.send_message(message.chat.id, end_message, reply_markup=keyboard_start)


# Default Reply
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    bot.send_message(message.chat.id, "Я умею только котиков показывать " + r'😾' , reply_markup=keyboard_start)
