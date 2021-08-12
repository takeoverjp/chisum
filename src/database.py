import sqlite3


class Database:
    def __init__(self, file_name):
        self._file_name = file_name
        self._connection = sqlite3.connect(self._file_name)

    def __del__(self):
        self._connection.close()
