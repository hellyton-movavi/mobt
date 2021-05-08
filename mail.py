import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import _thread as th

import time
import json

sets_file = open('settings.json', 'r')
SETTINGS = json.load(sets_file)
sets_file.close()


class Letter():

    def __init__(self, data, subject=''):
        self.data = data
        self.message = MIMEMultipart("alternative")
        self.message['Subject'] = subject
        self.message.attach(MIMEText(self.data, "html"))

    def send(self, reciever):
        reciever_mail = reciever
        sender_mail = SETTINGS['mail']['sender']
        password = SETTINGS['mail']['passw']

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as serv:
                serv.login(sender_mail, password)
                serv.sendmail(sender_mail, reciever_mail, self.message.as_string())
            return 0
        except Exception:
            return -1

# ! Only for debug reasons

# while True:
#     letter = Letter(open('mail-templates/reg.html', 'r').read())
#     letter.send('mbudko2@gmail.com')