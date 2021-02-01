# Copyright Max Budko (a.k.a. maxmine2, mxbdk)
import datetime
import os

import yaml
from flask import Flask, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

import mail

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
app.config['SQLALCHEMY_DATABASE_URI'] = SETTINGS['database']['address']

manager = Manager(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(), primary_key=True)
    nick = db.Column(db.String(96), nullable=False)
    mobile_operator_id = db.Column(db.Integer(), nullable=False)
    xp = db.Column(db.Integer(), primary_key=True)
    data = db.Column(db.Json)


if __name__ == '__main__':
    app.run()
