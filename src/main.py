from datetime import datetime

from src.count_controller import CountController
from src.database_count_repository import DatabaseCountRepository
from src.record_count_use_case_interactor import RecordCountUseCaseInteractor


def main():
    repository = DatabaseCountRepository(
        "chisum.db", "table1")
    interactor = RecordCountUseCaseInteractor(repository)
    controller = CountController(interactor)
    controller.record("testdata/libs.txt", datetime.now())


if __name__ == '__main__':
    main()
