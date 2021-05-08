import db


class Dashboard():
    def __init__(self, user_id: int, database: db.Database):
        self.user_id = user_id
        self.__database = database

        self.data = dict()

    def __get_history():
        