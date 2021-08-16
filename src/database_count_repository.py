import sqlite3
from datetime import datetime, timezone
from typing import List

from src.abstract_count_repository import AbstractCountRepository
from src.entity.count_entity import CountEntity


class DatabaseCountRepository(AbstractCountRepository):
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
            f'    WHERE TYPE=\'table\''
            f'        AND name=\'{self._table_name}\'')\
            .fetchone()[0] == 1

    def create_table(self):
        self._cursor.execute(
            f'CREATE TABLE {self._table_name}'
            '    (timestamp INTEGER, key TEXT, value INTEGER)'
        )
        self._connection.commit()

    def dump_master(self):
        print(self._cursor.execute(
            'SELECT * from sqlite_master')
            .fetchall())

    def save(self, counts: List[CountEntity]):
        for count in counts:
            self._cursor.execute(
                f'INSERT INTO {self._table_name}'
                '    (timestamp, key, value)'
                '    VALUES ('
                f'       {int(count.timestamp.timestamp())},'
                f'       "{count.key}",'
                f'       {count.value})')
        self._connection.commit()

    def _fetch(self, sql: str) -> List[CountEntity]:
        def row_to_count_entity(row) -> CountEntity:
            return CountEntity(datetime.fromtimestamp(
                row[0], tz=timezone.utc), row[1], row[2])

        return list(map(
            row_to_count_entity,
            self._cursor.execute(sql).fetchall()))

    def find_all(self) -> List[CountEntity]:
        return self._fetch(
            f'SELECT * from {self._table_name}')

    def find_by_timestamp(self, timestamp: datetime) -> List[CountEntity]:
        return self._fetch(
            f'SELECT * from {self._table_name}'
            f'    WHERE timestamp = {int(timestamp.timestamp())}')

    def get_timestamps(self, max_num: int) -> List[datetime]:
        timestamps = self._cursor.execute(
            f'SELECT DISTINCT timestamp from {self._table_name}'
            f'    ORDER BY timestamp DESC LIMIT {max_num}').fetchall()
        return list(map(lambda row:
                        datetime.fromtimestamp(row[0], tz=timezone.utc),
                        timestamps))


AbstractCountRepository.register(DatabaseCountRepository)
