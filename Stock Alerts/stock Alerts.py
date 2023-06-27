from twilio.rest import Client
import requests


def get_change(current, previous):
    if current == previous:
        return 100.0
    try:
        return (abs(current - previous) / previous) * 100.0
    except ZeroDivisionError:
        return 0


STOCK = "TSLA"
COMPANY_NAME = "Tesla"
NEWS_API_KEY = 'NEWS_API_KEY'
AA_API_KEY = 'AA_API_KEY'

# Twilio Setup
account_sid = 'account_sid'
auth_token = 'auth_token'
client = Client(account_sid, auth_token)
MY_PHONE = 'MY_PHONE'
TWILIO_PHONE = 'TWILIO_PHONE'

AA_params = {
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'symbol': STOCK,
    'outputsize': 'compact',
    'apikey': AA_API_KEY
}
AA_response = requests.get(url='https://www.alphavantage.co/query?', params=AA_params)
AA_response.raise_for_status()
AA_keys = list(AA_response.json()['Time Series (Daily)'].keys())
AA_data = [float(AA_response.json()['Time Series (Daily)'][AA_keys[0]]['4. close']),
           float(AA_response.json()['Time Series (Daily)'][AA_keys[1]]['1. open'])]
delta = int(round(get_change(AA_data[0], AA_data[1]), 1))
if AA_data[0] > AA_data[1]:
    alert = f'🔻 {delta}%'
elif AA_data[0] < AA_data[1]:
    alert = f'🔺{delta}%'

NEWS_params = {
    'apiKey': NEWS_API_KEY,
    'q': COMPANY_NAME,
    'pageSize': 3
}
NEWS_response = requests.get(url='https://newsapi.org/v2/top-headlines?', params=NEWS_params)
NEWS_response.raise_for_status()
NEWS_data = [
    f"{STOCK}: {alert} \nHeadline: {NEWS_response.json()['articles'][n]['title']}. \nBrief: {NEWS_response.json()['articles'][n]['description']}"
    for n in range(len(NEWS_response.json()['articles']))]

if delta >= 5:
    for data in NEWS_data:
        client.messages.create(
            from_=TWILIO_PHONE,
            to=MY_PHONE,
            body=data
        )
