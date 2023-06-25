import smtplib
from email.message import EmailMessage
import datetime as dt
from random import choice

msg = EmailMessage()

my_email = 'user@exmple.com'
sender = 'USERNAME'
password = ''
person = 'user@example.com'
subject = 'Happy Birthday'
message = ''

with open('quotes.txt', 'r') as file:
    data = file.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()


msg.set_content(choice(data))
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = person

current_day = dt.datetime.now().weekday()
if current_day == 1:
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.send_message(msg)
else:
    print("not monday", current_day)