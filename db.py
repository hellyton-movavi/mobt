# Copyright Max Budko (a.k.a. maxmine2, mxbdk), Lev Kvasnikov
#* This is the special file for working with databases
from os import terminal_size
import mysql.connector
import yaml

file = open('settings.yaml' 'a')
SETTINGS = yaml.load(file)
file.close()
del file

# conn = psycopg2.connect(database=SETTINGS['database']['database'],
#                         user=SETTINGS['database']['user'], password=SETTINGS['database']['pass'],
#                         host=SETTINGS['database']['host'], port=SETTINGS['database']['port'])

# cursor = conn.cursor()

