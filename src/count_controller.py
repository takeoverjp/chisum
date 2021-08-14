from datetime import datetime

from src.abstract_record_count_use_case import AbstractRecordCountUseCase
from src.count_entity import CountEntity
from src.record_count_input_data import RecordCountInputData


class CountController:
    input_boundary: AbstractRecordCountUseCase

    def __init__(self, input_boundary: AbstractRecordCountUseCase):
        self.input_boundary = input_boundary

    @classmethod
    def parse_snapshot(cls, file_path, timestamp):
        def parse_line(line):
            elem = line.split()
            return CountEntity(timestamp, elem[1], int(elem[0]))

        with open(file_path) as f:
            lines = [line.strip() for line in f.readlines()]
            counts = list(map(parse_line, lines))
        return counts

    def record(self, file_path: str, timestamp: datetime):
        input = RecordCountInputData()
        input.counts = self.parse_snapshot(file_path, timestamp)
        self.input_boundary.handle(input)
