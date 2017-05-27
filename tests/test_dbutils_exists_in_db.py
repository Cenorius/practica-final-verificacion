# -*- coding: utf-8 -*-

from .context import DBUtils

import mock
import unittest
from test_auxiliary_functions import get_fake_collection


class CheckDataExistsInDatabaseTestSuite(unittest.TestCase):
    """Test cases for checking if data exists or not in the database"""

    def test_exists_in_database(self):
        """Test if an element exists in the database or not"""
        objects = ["this", "is", "a", "test", "list"]

        # Prepare fake DB
        collection = get_fake_collection()
        collection.insert_one({'text': objects})

        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)

        # Let's pretend arguments are okay
        db.check_args_type = mock.MagicMock(return_value=True)

        # Check
        output = db.exists_in_db(objects)
        self.assertTrue(output)

    def test_not_exists_in_database(self):
        """Test if an element exists in the database or not"""

        # Prepare fake DB
        collection = get_fake_collection()

        db = DBUtils.DBUtils(collection)

        # Let's pretend arguments are okay
        db.check_args_type = mock.MagicMock(return_value=True)

        output = db.exists_in_db(["some", "random", "data"])
        self.assertFalse(output)

    def test_not_valid_type(self):
        """
        Test if an element exists in the database
        or not with an invalid type
        """

        # Prepare fake DB
        collection = get_fake_collection()

        db = DBUtils.DBUtils(collection)

        with self.assertRaises(Exception) as cm:
            db.exists_in_db("some random data")
        self.assertEqual("Invalid argument", str(cm.exception), "No exception raised")
