import requests
from twilio.rest import Client

account_sid = 'account_sid'
auth_token = "auth_token"
client = Client(account_sid, auth_token)

is_raining_today = False
OWM_Endpoint = 'https://api.openweathermap.org/data/2.5/onecall?'
api_key = 'api_key'
MY_NUMBER = 'MY NUMBER'
TWILIO_NUMBER = 'TWILIO_NUMBER'
# api_key = 'c7e91ad5a83ef4f6a41917b0e9ea6c0f'
lat = 32.754131
lon = -117.094070
exclude = 'current,minutely,daily,alerts'
weather_params = {
    'lat': lat,
    'lon': lon,
    'exclude': exclude,
    'appid': api_key
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = [weather['weather'][0]['id'] for weather in response.json()['hourly'][:12]]
for code in weather_data:
    if code <= 700:
        is_raining_today = True

if is_raining_today:
    is_raining_today = False
    message = client.messages.create(
        from_=TWILIO_NUMBER,
        body=' Its going to rain today bring a sweater😎',
        to=MY_NUMBER
    )
