import requests

url = "https://api.telegram.org/bot{token}/{method}".format(
    token="1280990087:AAHYwHfHmSQfvPz4T1bLrunes97gHpRaUwg",
    method = "setWebhook"
    #method="getWebhookinfo"
    #method = "deleteWebhook")

data = {"url": "https://functions.yandexcloud.net/d4ea2u645d8seikvq3u7"}

r = requests.post(url, data=data)
print(r.json())
 
