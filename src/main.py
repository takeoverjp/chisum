from datetime import datetime

import click

from src.count_controller import CountController
from src.database_count_repository import DatabaseCountRepository
from src.record_count_use_case_interactor import RecordCountUseCaseInteractor


@click.group()
def cmd():
    pass


@cmd.command()
@click.argument('source', type=str)
@click.argument('dest_database', type=str)
@click.argument('table', type=str)
def record(source, dest_database, table):
    repository = DatabaseCountRepository(
        dest_database, table)
    interactor = RecordCountUseCaseInteractor(repository)
    controller = CountController(interactor)
    controller.record(source, datetime.now())


def main():
    cmd()


if __name__ == '__main__':
    main()
