import requests
import os
import pandas as pd
from twilio.rest import Client

# define const
STOCK = 'TSLA'
COMPANY_NAME = 'Tesla Inc'
ALPHA_KEY = os.environ.get('ALPHA_KEY')
NEWS_KEY = os.environ.get('NEWS_KEY')
TWILIO_KEY = os.environ.get('TWILIO_KEY')
TWILIO_TOKEN = os.environ.get('TWILIO_TOKEN')
NUM_FROM = os.environ.get('NUM_FROM')
NUM_TO = os.environ.get('NUM_TO')
ALPHA_URL = 'https://www.alphavantage.co/query'
NEWS_URL = 'http://newsapi.org/v2/everything'

alpha_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': ALPHA_KEY
}

connection = requests.get(url=ALPHA_URL, params=alpha_params)
data = connection.json()
df = pd.DataFrame(data['Time Series (Daily)']).transpose()
df_close = df.iloc[:, 3]
df_close = df_close.astype('float')
daily_change = df_close[0]/df_close[1]
daily_change = round((daily_change - 1) * 100, 2)
current_date = df_close.index[0]

# if pct change is greater than 5% get news and send sms
if abs(daily_change) >= 5:
    news_params = {
        'q': STOCK,
        'from': current_date,
        'sortBy': 'popularity',
        'apiKey': NEWS_KEY
    }

    connection = requests.get(url=NEWS_URL, params=news_params)
    data = connection.json()
    article = data['articles'][0]
    source = article['source']['name']
    title = article['title']
    description = article['description']
    url = article['url']

    client = Client(TWILIO_KEY, TWILIO_TOKEN)
    message = client.messages \
                    .create(
                         body=f'{STOCK}: {daily_change}%\n{source}: {title}\n{description}\n{url}',
                         from_=NUM_FROM,
                         to=NUM_TO
                     )

    print(message.sid)
