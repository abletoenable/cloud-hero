#Echo telegram-bot for Yandex.Cloud CloudFunction

import requests
import json

# Telegram Bot Token
token = "TELEGRAM_BOT_TOKEN"


# handler
def point(event, context):
    body = json.loads(event['body'])
    chat_id = body['message']['from']['id']
    text = body['message']['text']
    send_message(chat_id, text)


#send message function
def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot' + token + '/' + 'sendMessage'
    data = {'chat_id': chat_id, 'text': text}
    r = requests.post(url, data=data)
