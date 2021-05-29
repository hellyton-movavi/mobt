import db
import datetime


class Dashboard():
    def __init__(self, user_id: int, database: db.Database):
        self.mobile_service_id = db.MobileServices.get_user_id()
        self.__database = database

        self.data = dict()

    def __get_history(self):
        self.__balance = db.History.gethistory(self.__database, furthest_time=datetime.datetime.utcnow() - datetime.timedelta(hours=1))
        self.__

    def __get_buildings(self):
        self.__buildings = db.Buildings.getbuildings(self.__database, user_id=self.mobile_service_id)

    def getall(self):
        self.__get_balance()
        self.__get_buildings()
        return {
            "balance": self.__balance,
            "buildings": self.__buildings,
        }
