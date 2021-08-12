import os
import unittest

from src.database import Database


class TestDataBase(unittest.TestCase):
    test_db_name = "test_database.db"

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
        db = Database(self.test_db_name, "items")

        # Assert
        self.assertTrue(os.path.isfile(self.test_db_name))
        self.assertTrue(db.has_table())

    def test_connect_exist_database(self):
        # SetUp
        db = Database(self.test_db_name, "items")
        self.assertTrue(os.path.isfile(self.test_db_name))

        # Execute
        db = Database(self.test_db_name, "items")

        # Assert
        self.assertTrue(os.path.isfile(self.test_db_name))
        self.assertTrue(db.has_table())


if __name__ == '__main__':
    unittest.main()
