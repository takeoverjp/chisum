import sqlite3


class Database:
    def __init__(self, file_name):
        self.file_name = file_name
        self.connection = sqlite3.connect(self.file_name)

    def __del__(self):
        self.connection.close()
