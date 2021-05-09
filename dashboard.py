import db
import datetime


class Dashboard():
    def __init__(self, user_id: int, database: db.Database):
        self.mobile_service_id
        self.__database = database

        self.data = dict()

    def __get_history():
        self.__income_history = db.History.gethisttory(self.__database, period_from=datetime.datetime.utcnow() - datetime.timedelta(hours=12),
                                                       period_to=datetime.datetime.utcnow(), records_type=RECORDS_TYPES['income'])

        self.__expenses_history = db.History.gethistory(self.__database, period_from=datetime.datetime.utcnow() - datetime.timedelta(hours=12),
                                                        period_to=datetime.datetime.utcnow(), records_type=RECORDS_TYPES['expenses'])

        self.__users_history = db.History.gethistory(self.__database, period_from=datetime.datetime.utcnow() - datetime.timedelta(hours=12),
                                                     period_to=datetime.datetime.utcnow(), records_type=RECORDS_TYPES['users'])

    def __get_buildings():
        self.__buildings = db.Buildings.getbuildings(self.__database, period_from=datetime.datetime.utcnow() - datetime.timedelta(hours=12),
                                                     period_to=datetime.datetime.utcnow())

    def getall():
        self.__get_history()
        self.__get_buildings()
        return {
            "income": self.__income_history,
            "expenses": self.__expenses_history,
            "users": self.__users_history,
            "buildings": self.__buildings
        }
