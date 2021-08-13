import sqlite3
from datetime import datetime, timezone
from typing import List
from src.count_entity import CountEntity
from src.storage_interface import StorageInterface


class StorageDatabase(StorageInterface):
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
            '  (timestamp REAL, key TEXT, value INTEGER)'
        )
        self._connection.commit()

    def dump_master(self):
        print(self._cursor.execute(
            'SELECT * from sqlite_master')
            .fetchall())

    def store(self, count: CountEntity):
        self._cursor.execute(
            f'INSERT INTO {self._table_name}'
            '  (timestamp, key, value)'
            '  VALUES ('
            f'   {count.timestamp.timestamp()},'
            f'   "{count.key}",'
            f'   {count.value})')
        self._connection.commit()

    def load_all(self) -> List[CountEntity]:
        return list(map(
            lambda ent: CountEntity(datetime.fromtimestamp(
                ent[0], tz=timezone.utc), ent[1], ent[2]),
            self._cursor.execute(
                f'SELECT * from {self._table_name}').fetchall()))


StorageInterface.register(StorageDatabase)
