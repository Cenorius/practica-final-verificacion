# -*- coding: utf-8 -*-

from .context import DBUtils
import unittest
from test_auxiliary_functions import get_fake_collection


class QueryDatabaseTestSuite(unittest.TestCase):
    """Test cases for querying the database"""

    def test_existing_data_query(self):
        """Test existing data query"""
        objects = ["my", "data", "hello", "world"]

        # Prepare fake DB
        collection = get_fake_collection()
        collection.insert_one({'text': objects})

        db = DBUtils.DBUtils(collection)

        output = db.query_db()
        self.assertEqual(len(output), 1)
        self.assertDictEqual(output[0], {u'text': objects})

    def test_not_existing_data_query(self):
        """Test not existing data query"""
        # Prepare fake DB
        collection = get_fake_collection()

        db = DBUtils.DBUtils(collection)

        output = db.query_db()
        self.assertEqual(output, [])
