# Copyright Max Budko (a.k.a. maxmine2, mxbdk), Lev Kvasnikov
import datetime
import os

import yaml
from flask import Flask, render_template, request, session, url_for, redirect

import mail
import sentry_sdk

sentry_sdk.init(
    "https://7580bf0467114c7e9afe2889bfba38f6@o570645.ingest.sentry.io/5717743",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

app = Flask(__name__)
setsfile = open('settings.yaml', 'r')
SETTINGS = yaml.load(setsfile)
setsfile.close()

file = open('accesskey.key', 'ab')
key = file.read()
if key != "":
    key = os.urandom(2 ** 32)
    file.write(key)
    file.close()

app.config['SECRET_KEY'] = key
del key
# app.config['SQLALCHEMY_DATABASE_URI'] = SETTINGS['database']['address']

database = db.Database(SETTINGS['database']['id'])

@app.route('/')
def mainpage():
    

@app.route('/api')
@app.route('/api/')
def redir_to_main_page():
    return redirect(url_for('/'))

@app.route('/api/login_page')
def get_login_page():
    return ''

@app.route('/api/login', methods=['POST'])
def login_page():
    return ''

@app.route('/api/init')
    

if __name__ == '__main__':
    app.run()
