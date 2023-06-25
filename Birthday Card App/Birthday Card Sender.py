from random import randint
import pandas as pd
import datetime as dt
import smtplib
from email.message import EmailMessage

"""
SETUP:
Fill out all the required information.

Follow the following steps or you will get an error.
- Enable 2FA on Google or other email host

Following steps for Google, if you're using other email look it up but should be a similar process.

- For Google, look up App Password on the accounts.google.com page after logging in
- Choose the custom app option and get a custom password for the app
- That will be you app password

"""

# Fill this information out to send the emails
SENDER = 'SENDER NAME'
USERNAME = 'EMAIL'
APP_PASSWORD = 'CUSTOM APP PASSWORD'
# This has to be replaced for different email hosts, Google it.
HOST = 'smtp.gmail.com'

# Getting the current day
now = dt.datetime.now()

# Reading and making the Dataframe into a dictionary without the index
birthdays = pd.read_csv('birthdays.csv').to_dict(orient='records')

# Going through all the indexes in the birthdays.csv file
for birthday in birthdays:
    # Returns true if the month and day match that of a person on the birthdays list
    someones_birthday_today = birthday['month'] == now.month and birthday['day'] == now.day
    if someones_birthday_today:
        # Chooses a letter
        letter = f'letter_templates/letter_{randint(1, 3)}.txt'
        # Opens the letter
        with open(letter, 'r') as letter_data:
            # Reads and replaces the [NAME] in letter
            raw_letter = letter_data.read()
            raw_letter = raw_letter.replace('[NAME]', birthday['name'])
        # Create the message in the email and all requirements
        msg = EmailMessage()
        msg.set_content(raw_letter)
        msg['Subject'] = 'Happy Birthday'
        msg['From'] = SENDER
        msg['To'] = birthday['email']
        # Opens up a new connection, logs in with the provided app password, and sends.
        with smtplib.SMTP(host=HOST, port=587) as connection:
            connection.starttls()
            connection.login(user=USERNAME, password=APP_PASSWORD)
            connection.send_message(msg)
