# -*- coding: utf-8 -*-

from .context import DBUtils

import mock
import unittest
from test_auxiliary_functions import get_fake_collection


class CheckArticleExistsInDatabaseTestSuite(unittest.TestCase):
    """Test cases for checking if data exists or not in the database"""

    def test_article_exists_in_database(self):
        """Test if an element exists in the database or not"""
        words = []
        date="1/2/3000"
        title="title"
        # Prepare fake DB
        collection = get_fake_collection()
        collection.insert_one({'date':date,'title': title,'words':words})

        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)
        db._is_date = mock.MagicMock(return_value=True)
        # Check
        output = db.exists_article_in_db(title,date)
        self.assertTrue(output)

    def test_article_not_exists_in_database(self):
        """Test if an element exists in the database or not"""

        # Prepare fake DB
        collection = get_fake_collection()

        db = DBUtils.DBUtils(collection)
        db._is_date = mock.MagicMock(return_value=True)

        output = db.exists_article_in_db('ey','1/2/3000')
        self.assertFalse(output)

    def test_date_format_incorrect(self):
        """Test if an element exists in the database or not"""

        # Prepare fake DB
        collection = get_fake_collection()

        db = DBUtils.DBUtils(collection)

        db._is_date = mock.MagicMock(return_value=False)

        with self.assertRaises(Exception) as cm:
            db.exists_article_in_db('ey',3)
        self.assertEqual("Date format is not valid", str(cm.exception), "No exception 'Date format is not valid' raised")