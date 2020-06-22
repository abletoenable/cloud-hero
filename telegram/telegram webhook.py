import requests

url = "https://api.telegram.org/bot{token}/{method}".format(
    token="TELEGRAM_BOT_TOKEN",
    method = "setWebhook"
    #method="getWebhookinfo"
    #method = "deleteWebhook"
)

data = {"url": "WEBHOOK_URL"}

r = requests.post(url, data=data)
print(r.json())
 
