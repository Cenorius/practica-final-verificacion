# -*- coding: utf-8 -*-

from .context import DBUtils
import unittest
from test_auxiliary_functions import get_fake_collection

class CleanDatabaseTestSuite(unittest.TestCase):
    """Test cases for cleaning up the database"""

    def test_clean_db_with_data(self):
        """Test if the db is cleaned correctly"""
        objects = ["my", "data", "hello", "world"]

        collection = get_fake_collection()
        collection.insert_one({'text': objects})

        db = DBUtils.DBUtils(collection)

        # Clean db
        db.clean_db()

        # Check if there is something left
        out = db.query_db()
        self.assertEqual(len(out),0)
        self.assertEqual(out,[])

    def test_clean_db_with_no_data(self):
        """Test if the db is cleaned correctly"""
        collection = get_fake_collection()

        db = DBUtils.DBUtils(collection)

        # Clean db
        db.clean_db()

        # Check if there is something left
        out = db.query_db()
        self.assertEqual(len(out),0)
        self.assertEqual(out,[])