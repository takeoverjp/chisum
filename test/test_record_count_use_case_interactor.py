from datetime import datetime, timezone
from src.entity.count_entity import CountEntity
import unittest

from src.in_memory_count_repository import InMemoryCountRepository
from src.record_count_input_data import RecordCountInputData
from src.record_count_use_case_interactor import RecordCountUseCaseInteractor


class TestRecordCountUseCaseInteractor(unittest.TestCase):
    def setUp(self) -> None:
        self.repository = InMemoryCountRepository()
        return super().setUp()

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
        ent0 = CountEntity(datetime(2020, 1, 1, 0, 0, 0,
                                    tzinfo=timezone.utc), "/bin/bash", 3)
        ent1 = CountEntity(datetime(2021, 2, 3, 4, 5, 6,
                                    tzinfo=timezone.utc), "/bin/sash", 4)
        ent2 = CountEntity(datetime(2022, 3, 4, 5, 6, 7,
                                    tzinfo=timezone.utc), "/bin/cash", 5)
        counts = []
        counts.append(ent0)
        counts.append(ent1)
        counts.append(ent2)
        input = RecordCountInputData(counts)

        # Execute
        interactor.handle(input)

        # Assert
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 3)
        self.assertIn(ent0, counts)
        self.assertIn(ent1, counts)
        self.assertIn(ent2, counts)
