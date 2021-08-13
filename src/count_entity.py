from datetime import datetime


class CountEntity:
    def __init__(self, timestamp: datetime, path: str, count: int):
        self.timestamp = timestamp
        self.path = path
        self.count = count

    def __str__(self) -> str:
        return f'{self.timestamp}, {self.path}, {self.count}'

    def __eq__(self, o: object) -> bool:
        return (self.timestamp == o.timestamp
                and self.path == o.path
                and self.count == o.count)
