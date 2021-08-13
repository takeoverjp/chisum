from typing import List
from src.count_entity import CountEntity


class RecordCountInputData:
    counts: List[CountEntity]

    def __init__(self):
        self.counts = []
