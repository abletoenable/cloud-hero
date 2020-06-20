import requests

url = "https://api.telegram.org/bot{token}/{method}".format(
    token="TOKEN",
    method = "setWebhook"
    #method = "deleteWebhook"
    #method = "getWebhookinfo"  
)

data = {
    "url": "WEBHOOK_URL"
}

r = requests.post(url, data = data)
print(r.json())
