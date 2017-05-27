# -*- coding: utf-8 -*-

from .context import DBUtils
import mock
import unittest
from test_auxiliary_functions import get_fake_collection


class CheckStoreInDatabaseTestSuite(unittest.TestCase):
    """Test cases for store in database"""

    def test_store_in_database(self):
        """Test store data in DB"""
        objects = ["this", "is", "a", "test", "list"]
        expected = {u'text': objects}

        # Prepare fake DB
        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        # Force non-existance
        db.exists_in_db = mock.MagicMock(return_value=False)

        output = db.store_in_db(objects)
        self.assertIsNotNone(output)

        # Test if it was saved
        data = db.query_db()
        self.assertEqual(len(data), 1, "Stored more data than expected")
        self.assertEqual(data[0], expected, "Data not stored correctly")

    def test_store_already_existing_in_database(self):
        """Test store something that already exists to de database"""

        # Prepare fake DB
        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        # Force existance of something
        db.exists_in_db = mock.MagicMock(return_value=True)

        with self.assertRaises(Exception) as cm:
            db.store_in_db(["this", "is", "a", "test", "list"])
        self.assertEqual("data already exists in DB", str(cm.exception), "No exception raised")

    def test_store_invalid_type_in_database(self):
        """Test store something with invalid type in the database"""

        # Prepare fake DB
        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        # Force invalid type
        db.check_args_type = mock.MagicMock(return_value=False)

        with self.assertRaises(Exception) as cm:
            db.store_in_db("invalid data type")
        self.assertEqual("Invalid argument", str(cm.exception), "No exception raised")
