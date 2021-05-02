# Copyright Max Budko (a.k.a. maxmine2, mxbdk), Lev Kvasnikov
# * This is the special file for working with databases
from os import terminal_size
import mysql.connector
import json
import random

file = open('settings.json', 'r')
SETTINGS = json.load(file)
print(SETTINGS)
file.close()
del file


# conn = psycopg2.connect(database=SETTINGS['database']['database'],
#                         user=SETTINGS['database']['user'], password=SETTINGS['database']['pass'],
#                         host=SETTINGS['database']['host'], port=SETTINGS['database']['port'])

# cursor = conn.cursor()


class Database():
    def __init__(self, sets):
        self.__db = mysql.connector.connect(
            host=sets['host'],
            user=sets['user'],
            password=sets['pass'],
            database=sets['database'],
            auth_plugin='caching_sha2_password'
        )
        self.__cursor = self.__db.cursor()

    def insert(self, query):
        self.__cursor.execute(query)
        self.__db.commit()

    def get(self, query):
        self.__cursor.execute(query)
        return self.__cursor.fetchall()


class Users():
    @staticmethod
    def create_user(database: Database, nick: str, mail: str, password_hash: str, mobile_service_id=None) -> int:
        #  Первый запрос - создать таблицу Users
        level = 1
        xp = 0
        database.insert(
            f"""INSERT INTO users (mobile_service_id, level, xp) VALUES ({mobile_service_id if mobile_service_id != None else 'null'}, {level}, {xp})""")
        #  Создание новой записи в таблицу(строка users)
        id_user = database.get(f"""SELECT LAST_INSERT_ID();""")[0][0]
        #  get - запрос к базе данных

        #  Создание новой записи (login_users) в базе данных
        database.insert(
            f"INSERT INTO login_users (id, nick, mail, psword_hash) VALUES({id_user}, '{nick}', '{mail}', '{password_hash}')")
        return id_user

    @staticmethod
    def get_users_passw_hash(database: Database, nick: str):
        #  Нужно обратиться к таблице login_users, запросить password_hush для записи nick
        password_hash = database.get(
            f"""SELECT password_hash FROM login_users WHERE nickname = {nick}""")[0][0]
        return password_hash


class MobileServices():
    @staticmethod
    def create_mobile_service(database: Database, service_name: str, user_id: int):
        user_attraction = 1.0
        database.insert(
            f"""INSERT INTO mobile_services (service_name, users, user_attraction) VALUES('{service_name}', {user_id}, {user_attraction})""")
        mobile_service_id = database.get(f"""SELECT LAST_INSERT_ID();""")[0][0]
        return mobile_service_id


class Buildings():
    @staticmethod
    def create_building(database: Database, mobile_service_id: int, building_type: int, building_model: int, lan: float, lon: float) -> int:
        database.insert(
            f"""INSERT INTO buildings (mobile_service_id, building_type, building_model, lan, lon) VALUES ({mobile_service_id}, {building_type}, {building_model}, {lan}, {lon});""")
        building_id = database.get(f"""SELECT LAST_INSERT_ID();""")[0][0]
        return building_id
