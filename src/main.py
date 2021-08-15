from datetime import datetime

import click

from src.database_count_repository import DatabaseCountRepository
from src.record_count_controller import RecordCountController
from src.record_count_use_case_interactor import RecordCountUseCaseInteractor
from src.report_count_controller import ReportCountController
from src.report_count_presenter import ReportCountPresenter
from src.report_count_use_case_interactor import ReportCountUseCaseInteractor


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
    controller = RecordCountController(interactor)
    controller.run(source, datetime.now())


@cmd.command()
@click.argument('database', type=str)
@click.argument('table', type=str)
def report(database, table):
    repository = DatabaseCountRepository(
        database, table)
    presenter = ReportCountPresenter()
    interactor = ReportCountUseCaseInteractor(repository, presenter)
    controller = ReportCountController(interactor)
    controller.run()


def main():
    cmd()


if __name__ == '__main__':
    main()
