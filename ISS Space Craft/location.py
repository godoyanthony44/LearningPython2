import requests
from datetime import datetime
from math import isclose
from time import sleep
from email.message import EmailMessage
import smtplib

LAT = 000.000
LNG = -000.000

parameters = {
    'lat': LAT,
    'lng': LNG,
    'formatted': 0
}

SENDER = 'Space Shuttle Look Program'
USERNAME = 'EMAIL'
APP_PASSWORD = 'APP PASSWORD'
# This has to be replaced for different email hosts, Google it.
HOST = 'smtp.gmail.com'
TO = 'EMAIL'


def is_time():
    response = requests.get(url='http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    latitude = float(response.json()['iss_position']['latitude'])
    longitude = float(response.json()['iss_position']['longitude'])
    location = (latitude, longitude)

    response2 = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
    response2.raise_for_status()
    data = response2.json()
    sunrise = [int(n) for n in (data['results']['sunrise'].split('T')[1].split('+'))[0].split(':')]
    sunset = [int(n) for n in (data['results']['sunset'].split('T')[1].split('+'))[0].split(':')]
    time_now = [int(n) for n in str(datetime.utcnow()).split(' ')[1].split('.')[0].split(':')]

    if time_now[0] <= sunrise[0] and time_now[0] >= sunset[0]:
        if isclose(LAT, latitude, rel_tol=5) and LNG == isclose(LNG, longitude, rel_tol=5):
            return True
        else:
            return False
    else:
        return False


while not is_time():
    if is_time():

        msg = EmailMessage()
        msg.set_content("Look Up Now \n The Space shuttle is right above you \n")
        msg['Subject'] = 'Look up the Space Shuttle is near.'
        msg['From'] = SENDER
        msg['To'] = TO
        with smtplib.SMTP(host=HOST, port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=APP_PASSWORD)
            connection.send_message(msg)
    else:
        print('waiting')
    sleep(20)
