import sqlite3


class Database:
    def __init__(self, file_name, table_name):
        self._file_name = file_name
        self._table_name = table_name
        self._connection = sqlite3.connect(self._file_name)
        self._cursor = self._connection.cursor()
        if not self.has_table():
            self.create_table()

    def __del__(self):
        self._connection.close()

    def has_table(self):
        return self._cursor.execute(
            'SELECT COUNT(*) from sqlite_master'
            f'  WHERE TYPE=\'table\''
            f'    AND name=\'{self._table_name}\'')\
            .fetchone()[0] == 1

    def create_table(self):
        self._cursor.execute(
            f'CREATE TABLE {self._table_name}'
            '  (timestamp TEXT, path TEXT, count INTEGER)'
        )
        self._connection.commit()

    def dump_master(self):
        print(self._cursor.execute(
            'SELECT * from sqlite_master')
            .fetchall())
