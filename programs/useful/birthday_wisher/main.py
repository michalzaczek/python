import pandas as pd
from datetime import *
from random import randint
import smtplib

df = pd.read_csv('birthdays.csv')
now = datetime.now()
bd = df[(df.month == now.month) & (df.day == now.day)]

for index, row in bd.iterrows():

    name = row['name']
    email = row['email']
    number = randint(1, 3)

    with open('letter_templates/letter_' + str(number) + '.txt', 'r') as file:
        msg = file.read()

    msg = msg.replace('[NAME]', name)

    connection = smtplib.SMTP(host='smtp.gmail.com', port=587)
    connection.starttls()
    connection.login(user='username', password='******')
    connection.sendmail(from_addr='Michal', to_addrs=email, msg='Subject:Happy Birthday!\n' + msg)
    connection.close()
