from datetime import datetime, timedelta, timezone
import os
from src.count_controller import CountController
import unittest

from src.database_count_repository import DatabaseCountRepository
from src.record_count_use_case_interactor import RecordCountUseCaseInteractor


class TestCountController(unittest.TestCase):
    test_db_name = "test.db"
    test_table_name = "counts"

    def setUp(self) -> None:
        if os.path.isfile(self.test_db_name):
            os.unlink(self.test_db_name)
        self.repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)
        self.interactor = RecordCountUseCaseInteractor(self.repository)
        return super().setUp()

    def tearDown(self) -> None:
        if os.path.isfile(self.test_db_name):
            os.unlink(self.test_db_name)
        return super().tearDown()

    def test_create(self):
        # Execute
        CountController(self.interactor)

    def test_record_once(self):
        controller = CountController(self.interactor)

        # Execute
        controller.record("testdata/counts0.txt",
                          datetime(2020, 1, 1,
                                   tzinfo=timezone.utc))

        # Assert
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 9)

    def test_record_multi(self):
        controller = CountController(self.interactor)
        time1 = datetime(2020, 1, 1, tzinfo=timezone.utc)
        time2 = time1 + timedelta(days=1)

        # Execute
        controller.record("testdata/counts0.txt", time1)
        controller.record("testdata/counts1.txt", time2)

        # Assert
        counts = self.repository.find_by_timestamp(time1)
        self.assertEqual(len(counts), 9)
        counts = self.repository.find_by_timestamp(time2)
        self.assertEqual(len(counts), 9)
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 18)
