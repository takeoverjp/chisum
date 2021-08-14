import os
import unittest

from src.database_count_repository import DatabaseCountRepository
from src.report_count_use_case_interactor import ReportCountUseCaseInteractor


class TestReportCountUseCaseInteractor(unittest.TestCase):
    test_db_name = "test.db"
    test_table_name = "counts"

    def setUp(self) -> None:
        if os.path.isfile(self.test_db_name):
            os.unlink(self.test_db_name)
        self.repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)
        return super().setUp()

    def tearDown(self) -> None:
        if os.path.isfile(self.test_db_name):
            os.unlink(self.test_db_name)
        return super().tearDown()

    def test_create(self):
        # Execute
        ReportCountUseCaseInteractor(self.repository)
