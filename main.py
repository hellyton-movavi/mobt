# Copyright Max Budko (a.k.a. maxmine2, mxbdk), Lev Kvasnikov
import datetime
import os

import json
from flask import Flask, render_template, request, session, url_for, redirect

import db
import mail
import tokenserver
import sentry_sdk

sentry_sdk.init(
    "https://7580bf0467114c7e9afe2889bfba38f6@o570645.ingest.sentry.io/5717743",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

app = Flask(__name__)
setsfile = open('settings.json', 'r')
SETTINGS = json.load(setsfile)
setsfile.close()

file = open('accesskey.key', 'a+b')
key = file.read()
if key == b'':
    key = os.urandom(2 ** 16)
    file.write(key)
    file.close()

app.config['SECRET_KEY'] = key
del key, file

file = open('jwtkey.pem', 'a+b')
jwtkey = file.read()
if jwtkey == b'':
    jwtkey = os.urandom(2 ** 10)
    file.write(f'{jwtkey}'.encode())
    file.close()


# app.config['SQLALCHEMY_DATABASE_URI'] = SETTINGS['database']['address']

database = db.Database(SETTINGS['database'])


@app.route('/')
def mainpage():
    if 'mobile_tycoon' not in session:
        session_id = session['mobile_tycoon_ident']


@app.route('/api')
@app.route('/api/')
def redir_to_main_page():
    return redirect(url_for('/'))


@app.route('/api/login_page')
def get_login_page():
    return


@app.route('/api/login', methods=['POST'])
def login_page():
    global jwtkey
    # TODO Аутентификация по логину и паролю
    # ? Делать Magic Link?

    # * Выдача JWT-токена
    # jwttoken = tokenserver.Token.generate(issuedat=datetime.datetime.utcnow(), expires=datetime.datetime.utcnow() + datetime.timedelta(hours=12),
    #                                       issuer='Mobile Tycoon Login API', algorithm='RS512', subject=user_id, key=jwtkey)
    return ''


if __name__ == '__main__':
    app.run()
