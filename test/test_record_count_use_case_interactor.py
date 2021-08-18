import unittest
from datetime import datetime, timezone

from src.entity.count_entity import CountEntity
from src.interface_adapter.in_memory_count_repository import \
    InMemoryCountRepository
from src.use_case.record_count_input_data import RecordCountInputData
from src.use_case.record_count_use_case_interactor import \
    RecordCountUseCaseInteractor


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
        date = datetime(2020, 1, 1, tzinfo=timezone.utc)
        input = RecordCountInputData(date, [])

        # Execute
        interactor.handle(input)

        # Assert
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 0)

    def test_handle_multi_input(self):
        # Setup
        interactor = RecordCountUseCaseInteractor(self.repository)
        date = datetime(2020, 1, 1, tzinfo=timezone.utc)
        ent0 = CountEntity(date, "/bin/bash", 3)
        ent1 = CountEntity(date, "/bin/sash", 4)
        ent2 = CountEntity(date, "/bin/cash", 5)
        counts = [ent0, ent1, ent2]
        input = RecordCountInputData(date, counts)

        # Execute
        interactor.handle(input)

        # Assert
        counts = self.repository.find_all()
        self.assertEqual(len(counts), 3)
        self.assertIn(ent0, counts)
        self.assertIn(ent1, counts)
        self.assertIn(ent2, counts)
