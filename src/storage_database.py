import sqlite3
from datetime import datetime, timezone
from src.entity import Entity


class StorageDatabase:
    def __init__(self, file_name: str, table_name: str):
        self._file_name = file_name
        self._table_name = table_name
        self._connection = sqlite3.connect(self._file_name)
        # self._connection.set_trace_callback(print)
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

    def store(self, entity: Entity):
        self._cursor.execute(
            f'INSERT INTO {self._table_name}'
            '  (timestamp, path, count)'
            '  VALUES ('
            f'   "{entity.timestamp.timestamp()}",'
            f'   "{entity.path}",'
            f'   {entity.count})')
        self._connection.commit()

    def load_all(self):
        return list(map(
            lambda ent: Entity(datetime.fromtimestamp(
                float(ent[0]), tz=timezone.utc), ent[1], int(ent[2])),
            self._cursor.execute(
                f'SELECT * from {self._table_name}').fetchall()))
