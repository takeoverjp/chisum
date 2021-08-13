from datetime import datetime, timezone
import os
from src.count_entity import CountEntity
import unittest

from src.database_count_repository import DatabaseCountRepository
from src.record_count_input_data import RecordCountInputData
from src.record_count_use_case_interactor import RecordCountUseCaseInteractor


class TestRecordCountUseCaseInteractor(unittest.TestCase):
    test_db_name = "test_database.db"
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
        RecordCountUseCaseInteractor(self.repository)

    def test_handle_empty(self):
        # Setup
        interactor = RecordCountUseCaseInteractor(self.repository)
        input = RecordCountInputData()

        # Execute
        interactor.handle(input)

        # Assert
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 0)

    def test_handle_multi_input(self):
        # Setup
        interactor = RecordCountUseCaseInteractor(self.repository)
        input = RecordCountInputData()
        ent0 = CountEntity(datetime(2020, 1, 1, 0, 0, 0,
                                    tzinfo=timezone.utc), "/bin/bash", 3)
        ent1 = CountEntity(datetime(2021, 2, 3, 4, 5, 6,
                                    tzinfo=timezone.utc), "/bin/sash", 4)
        ent2 = CountEntity(datetime(2022, 3, 4, 5, 6, 7,
                                    tzinfo=timezone.utc), "/bin/cash", 5)
        input.counts.append(ent0)
        input.counts.append(ent1)
        input.counts.append(ent2)

        # Execute
        interactor.handle(input)

        # Assert
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 3)
        self.assertIn(ent0, counts)
        self.assertIn(ent1, counts)
        self.assertIn(ent2, counts)
