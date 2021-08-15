import os
import unittest
from datetime import datetime, timezone

from src.count_entity import CountEntity
from src.database_count_repository import DatabaseCountRepository


class TestDatabaseCountRepository(unittest.TestCase):
    test_db_name = "test.db"
    test_table_name = "counts"

    def setUp(self) -> None:
        if os.path.isfile(self.test_db_name):
            os.unlink(self.test_db_name)
        self.assertFalse(os.path.isfile(self.test_db_name))
        return super().setUp()

    def tearDown(self) -> None:
        if os.path.isfile(self.test_db_name):
            os.unlink(self.test_db_name)
        return super().tearDown()

    def test_create_database(self):
        # Execute
        repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)

        # Assert
        self.assertTrue(os.path.isfile(self.test_db_name))
        self.assertTrue(repository.has_table())

    def test_connect_exist_database(self):
        # SetUp
        DatabaseCountRepository(self.test_db_name, self.test_table_name)
        self.assertTrue(os.path.isfile(self.test_db_name))

        # Execute
        repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)

        # Assert
        self.assertTrue(os.path.isfile(self.test_db_name))
        self.assertTrue(repository.has_table())

    def test_no_item_after_creation(self):
        # SetUp
        repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)

        # Execute
        counts = repository.find_all()

        # Assert
        self.assertEqual(len(counts), 0)

    def test_save_one_item(self):
        # SetUp
        repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)

        # Execute
        ent = CountEntity(datetime(2020, 1, 1, 0, 0, 0,
                                   tzinfo=timezone.utc), "/bin/bash", 3)
        repository.save([ent])

        # Assert
        counts = repository.find_all()
        self.assertEqual(len(counts), 1)
        self.assertEqual(counts[0], ent)

    def test_save_multi_items(self):
        # SetUp
        repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)

        # Execute
        ent0 = CountEntity(datetime(2020, 1, 1, 0, 0, 0,
                                    tzinfo=timezone.utc), "/bin/bash", 3)
        ent1 = CountEntity(datetime(2021, 2, 3, 4, 5, 6,
                                    tzinfo=timezone.utc), "/bin/sash", 4)
        ent2 = CountEntity(datetime(2022, 3, 4, 5, 6, 7,
                                    tzinfo=timezone.utc), "/bin/cash", 5)
        repository.save([ent0, ent1, ent2])

        # Assert
        counts = repository.find_all()
        self.assertEqual(len(counts), 3)
        self.assertIn(ent0, counts)
        self.assertIn(ent1, counts)
        self.assertIn(ent2, counts)

    def test_find_by_timestamp(self):
        # SetUp
        repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)

        ent0 = CountEntity(datetime(2020, 1, 1, 0, 0, 0,
                                    tzinfo=timezone.utc), "/bin/bash", 3)
        ent1 = CountEntity(datetime(2021, 2, 3, 4, 5, 6,
                                    tzinfo=timezone.utc), "/bin/sash", 4)
        ent2 = CountEntity(datetime(2022, 3, 4, 5, 6, 7,
                                    tzinfo=timezone.utc), "/bin/cash", 5)
        repository.save([ent0, ent1, ent2])

        # Execute
        counts = repository.find_by_timestamp(datetime(2020, 1, 1, 0, 0, 0,
                                                       tzinfo=timezone.utc))

        # Assert
        self.assertEqual(len(counts), 1)
        self.assertIn(ent0, counts)
        self.assertNotIn(ent1, counts)
        self.assertNotIn(ent2, counts)

    def test_get_timestamps(self):
        # SetUp
        repository = DatabaseCountRepository(
            self.test_db_name, self.test_table_name)
        dates = [datetime(2020, 1, 1, tzinfo=timezone.utc),
                 datetime(2020, 1, 2, tzinfo=timezone.utc),
                 datetime(2020, 1, 3, tzinfo=timezone.utc)]
        counts = list(map(lambda date: CountEntity(date, "key", 1), dates))
        repository.save(counts)

        # Execute
        timestamps = repository.get_timestamps(2)

        # Assert
        self.assertEqual(len(timestamps), 2)
        self.assertEqual(timestamps[0], dates[2])
        self.assertEqual(timestamps[1], dates[1])


if __name__ == '__main__':
    unittest.main()
