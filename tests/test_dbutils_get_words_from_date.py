# -*- coding: utf-8 -*-

from .context import DBUtils

import mock
import unittest
from test_auxiliary_functions import get_fake_collection


class CheckGetWordsInDatabaseTestSuite(unittest.TestCase):

    def test_not_exists_data_in_database(self):

        words = [{"word":"mal","count":7},{"word":"bien","count":6}]
        date="1/2/1000"
        title="title"

        title2="title2"

        expected=[{u'count': 14.0, u'_id': u'mal'},{u'count': 12.0, u'_id': u'bien'}]
        # Prepare fake DB
        collection = get_fake_collection()
        collection.insert_one({'date':date,'title': title,'words':words})
        collection.insert_one({'date':date,'title': title2,'words':words})

        
        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)
        db._is_date = mock.MagicMock(return_value=True)

        # Check
        output = db.get_words_from_date(date)
        
        self.assertEqual(output,expected,output)

    def test_exists_data_in_database(self):

        date="1/2/1000"
        expected=[]
        # Prepare fake DB
        collection = get_fake_collection()

        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)
        db._is_date = mock.MagicMock(return_value=True)

        # Check
        output = db.get_words_from_date(date)
        self.assertEqual(output,expected,output)

    def test_incorrect_type(self):

        date=1
        # Prepare fake DB
        collection = get_fake_collection()

        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)
        db._is_date = mock.MagicMock(return_value=False)

        with self.assertRaises(Exception) as cm:
            db.get_words_from_date(date)
        self.assertEqual("Date format is not valid", str(cm.exception), "No exception 'Date format is not valid' raised")

