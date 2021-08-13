from datetime import datetime


class CountEntity:
    def __init__(self, timestamp: datetime, key: str, value: int):
        self.timestamp = timestamp
        self.key = key
        self.value = value

    def __str__(self) -> str:
        return f'{self.timestamp}, {self.key}, {self.value}'

    def __eq__(self, o: object) -> bool:
        return (self.timestamp == o.timestamp
                and self.key == o.key
                and self.value == o.value)
