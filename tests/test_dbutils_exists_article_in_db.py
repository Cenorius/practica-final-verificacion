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
        date="1/2/3"
        title="title"
        # Prepare fake DB
        collection = get_fake_collection()
        collection.insert_one({'date':date,'title': title,'words':words})

        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)

        # Check
        output = db.exists_article_in_db(title,date)
        self.assertTrue(output)

    def test_article_not_exists_in_database(self):
        """Test if an element exists in the database or not"""

        # Prepare fake DB
        collection = get_fake_collection()

        db = DBUtils.DBUtils(collection)

        output = db.exists_article_in_db('ey','1/2/3')
        self.assertFalse(output)

