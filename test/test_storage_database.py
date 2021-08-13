import os
import unittest
from datetime import datetime, timezone

from src.entity import Entity
from src.storage_database import StorageDatabase


class TestDataBase(unittest.TestCase):
    test_db_name = "test_database.storage"
    test_table_name = "entities"

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
        storage = StorageDatabase(self.test_db_name, self.test_table_name)

        # Assert
        self.assertTrue(os.path.isfile(self.test_db_name))
        self.assertTrue(storage.has_table())

    def test_connect_exist_database(self):
        # SetUp
        StorageDatabase(self.test_db_name, self.test_table_name)
        self.assertTrue(os.path.isfile(self.test_db_name))

        # Execute
        storage = StorageDatabase(self.test_db_name, self.test_table_name)

        # Assert
        self.assertTrue(os.path.isfile(self.test_db_name))
        self.assertTrue(storage.has_table())

    def test_no_item_after_creation(self):
        # SetUp
        storage = StorageDatabase(self.test_db_name, self.test_table_name)

        # Execute
        entities = storage.load_all()

        # Assert
        self.assertEqual(len(entities), 0)

    def test_store_one_item(self):
        # SetUp
        storage = StorageDatabase(self.test_db_name, self.test_table_name)

        # Execute
        ent = Entity(datetime(2020, 1, 1, 0, 0, 0,
                     tzinfo=timezone.utc), "/bin/bash", 3)
        storage.store(ent)

        # Assert
        entities = storage.load_all()
        self.assertEqual(len(entities), 1)
        self.assertEqual(entities[0], ent)

    def test_store_multi_items(self):
        # SetUp
        storage = StorageDatabase(self.test_db_name, self.test_table_name)

        # Execute
        ent0 = Entity(datetime(2020, 1, 1, 0, 0, 0,
                               tzinfo=timezone.utc), "/bin/bash", 3)
        ent1 = Entity(datetime(2021, 2, 3, 4, 5, 6,
                               tzinfo=timezone.utc), "/bin/sash", 4)
        ent2 = Entity(datetime(2022, 3, 4, 5, 6, 7,
                               tzinfo=timezone.utc), "/bin/cash", 5)
        storage.store(ent0)
        storage.store(ent1)
        storage.store(ent2)

        # Assert
        entities = storage.load_all()
        self.assertEqual(len(entities), 3)
        self.assertIn(ent0, entities)
        self.assertIn(ent1, entities)
        self.assertIn(ent2, entities)


if __name__ == '__main__':
    unittest.main()
