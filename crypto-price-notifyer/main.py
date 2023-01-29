import time
import os
import requests

refreshTime = 3

def message(title, content):
    os.system('notify-send "' + title + '" "' + content + '"')


# price = 0
def check_price():
    url = 'https://api.coingecko.com/api/v3/exchange_rates'
    response = requests.get(url)
    marketData = response.json()

    current_price = round(marketData.get('rates').get('usd').get('value'), 0)
    content = "BTC alert $ " + str(current_price)
    message('Price alert', content)

    return current_price

while True:
    time.sleep(refreshTime)
    price = check_price()
