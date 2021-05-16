# Copyright Max Budko (a.k.a. maxmine2, mxbdk), Lev Kvasnikov
# * This is the special file for working with databases
from os import terminal_size
import mysql.connector
import json
import random
from staticparams import *
print(SETTINGS)


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
        # * Нужно обратиться к таблице login_users, запросить password_hash для записи nickname
        if not Users.user_exists(nick):
            return -1
        password_hash = database.get(
            f"""SELECT password_hash FROM login_users WHERE nick = {nick}""")[0][0]
        return password_hash

    @staticmethod
    def user_exists(database: Database, nick: str):
        return bool(database.get(f"""SELECT id, nick FROM users WHERE nick={nick}""")[0][0])

    @staticmethod
    def userid_by_mail(database: Database, mail: str):
        if not Users.user_exists(Users.nick_by_mail(database, mail)):
            return -1
        return database.get(f"""SELECT id FROM users WHERE mail={mail}""")


    @staticmethod
    def userid_by_nick(database: Database, nick: str) -> int:
        if database.get(f"""SELECT id FROM users WHERE nick={nick}imp""")[0][0]:
            return -1

        id = database.get(f"""SELECT id FROM users WHERE nick={nick}""")[0][0]
        return id

    @staticmethod
    def nick_by_mail(database: Database, mail: str):
        if not database.get(f"""SELECT nick FROM users WHERE mail={mail}""")[0][0]:
            return -1

        nick = database.get(f"""SELECT nick FROM users WHERE mail={mail}""")[0][0]
        return nick



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
        database.insert(f"""INSERT INTO buildings (mobile_service_id, building_type, building_model, lan, lon) VALUES ({mobile_service_id}, {building_type} {building_model}, {lan}, {lon})""")
        building_id = database.get(f"""SELECT LAST_INSERT_ID();""")[0][0]
        return building_id

    def getbuildings(database: Database, mobile_service_id: int):
        buildings = database.get(f"""SELECT * FROM buildings WHERE mobile_service_id = {mobile_service_id}""")[0]
        return {
            "buildings": [{
                "id": building[0],
                "type": building[2],
                "lan": building[4],
                "lon": building[5]
            } for building in buildings]
        }
        
class History():
    @staticmethod
    def gethistory(database):
        pass