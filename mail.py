import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import json

sets_file = open('settings.json', 'r')
SETTINGS = json.load(sets_file)
sets_file.close()


class Letter():

    def __init__(self, data):
        self.data = data
        self.message = MIMEMultipart("alternative")
        self.message.attach(MIMEText(self.data, "html"))

    def send(self, reciever):
        reciever_mail = reciever
        sender_mail = SETTINGS['mail']['sender']
        password = SETTINGS['mail']['passw']

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as serv:
            serv.login(sender_mail, password)
            serv.sendmail(sender_mail, reciever_mail, self.message.as_string())
