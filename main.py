# Copyright Max Budko (a.k.a. maxmine2, mxbdk), Lev Kvasnikov
import sentry_sdk


sentry_sdk.init(
    "https://7580bf0467114c7e9afe2889bfba38f6@o570645.ingest.sentry.io/5717743",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

import datetime
import os

import json
from flask import Flask, render_template, request, url_for, redirect
from werkzeug.security import check_password_hash, generate_password_hash

import db
import mail
import mail_creator
import base64
import tokenserver
from staticparams import *

app = Flask(__name__)

file = open('accesskey.key', 'a+b')
key = file.read()
if key == b'':
    key = os.urandom(2 ** 16)
    file.write(key)
    file.close()

app.config['SECRET_KEY'] = key
del key, file

file = open('jwtkey.pem', 'r')
jwtkey = file.read()
file.close()

# app.config['SQLALCHEMY_DATABASE_URI'] = SETTINGS['database']['address']

database = db.Database(SETTINGS['database'])


@app.route('/')
def mainpage():
    token = request.form.get('token')
    data_tkn = tokenserver.verify_token(token)
    if data_tkn != -1:
        if data_tkn['iss'] == 'Mobile Tycoon Login API':
            user_id = data_tkn['sub']
            dashbrd = dashboard.Dashboard(user_id, database)
            return {'status': 'success', 'data': dashbrd.getall()}

        else:
            return {'status': 'error', 'error': 'bad_token'}
    else:
        return {'status': 'error', 'error': 'bad_token'}

@app.route('/api')
@app.route('/api/')
def redir_to_main_page():
    return redirect(url_for('/'))


@app.route('/api/login_page')
def get_login_page():
    return


@app.route('/api/login/clicklink')
def login_via_magiclink():
    global jwtkey
    mail_addr = request.form.get('mail')
    user_id = db.Users.userid_by_mail(mail_addr)
    if user_id == -1:
        return {'status': 'error', 'error': 'mail_incorrect'}

    jwt_clicklink_key = tokenserver.Token.generate(issuedat=datetime.datetime.utcnow(), expires=datetime.datetime.utcnow() + datetime.timedelta(hours=1),
                                                   issuer='Mobile Tycoon ClickLink Login API', algorithm='RS256', subject=user_id, key=jwtkey)

    templated_letter = mail_creator.TemplateLetter(MAILTEMPLATES['clicklink'])
    templated_letter.render(
        loginurl=f'https://{SETTINGS["app"]["base_domain"]}/lg/clicklink/{base64.b64encode(jwt_clicklink_key.encode("ascii")).decode("ascii")}')
    sendable_letter = mail.Letter(str(templated_letter))
    result = sendable_letter.send(mail_addr)
    return {'status': 'error', 'error' : "couldnt_send_letter"} if result == -1 else {'status': 'success'}


@app.route('/lg/clicklink/<id>')
def magiclink_login_apprv(id):
    token = base_64.b64decode(id.encode('ascii')).decode('ascii')
    token_data = tokenserver.verify(token)
    if token_data == -1:
        return {'status': 'error', 'error': 'bad_link'}
    
    if token_data['iss'] != 'Mobile Tycoon ClickLink Login API':
        return redirect()
    return


@app.route('/api/login/mailpass', methods=['POST'])
def login_via_mailpass():
    global jwtkey
    login = request.form.get("login")
    passw = request.form.get("passw")

    result = db.Users.get_users_passw_hash(db, login)
    if result != -1:
        if check_password_hash(result, passw):
            jwttoken = tokenserver.Token.generate(issuedat=datetime.datetime.utcnow(), expires=datetime.datetime.utcnow() + datetime.timedelta(hours=12),
                                                  issuer = 'Mobile Tycoon Login API', algorithm = 'RS512', subject = user_id, key = jwtkey)

            return {'status': 'success', 'token': jwttoken}
        else:
            return {'status': 'error', 'error': 'password_incorrect'}
    else:
        return {'status': 'error', 'error': 'user_not_found'}

@app.route('/api/reg')
def reg_link():
    

@app.route('/api/applc/update'):
def app_upd():
    return json.dumps({"latest": '0.1'})
if __name__ == '__main__':
    app.run()
