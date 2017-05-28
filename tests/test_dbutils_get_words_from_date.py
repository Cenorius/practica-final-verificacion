# -*- coding: utf-8 -*-

from .context import DBUtils

import mock
import unittest
from test_auxiliary_functions import get_fake_collection


class CheckGetWordsInDatabaseTestSuite(unittest.TestCase):

    def test_not_exists_data_in_database(self):

        words = [{"word":"mal","count":7},{"word":"bien","count":6}]
        date="1/2/3"
        title="title"

        expected=[{u'count': 7.0, u'_id': u'mal'},{u'count': 6.0, u'_id': u'bien'}]
        # Prepare fake DB
        collection = get_fake_collection()
        collection.insert_one({'date':date,'title': title,'words':words})

        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)

        # Check
        output = db.get_words_from_date(date)
        
        self.assertEqual(output,expected,output)

    def test_exists_data_in_database(self):

        date="1/2/3"
        expected=[]
        # Prepare fake DB
        collection = get_fake_collection()

        # Get DBUtils with fake DB
        db = DBUtils.DBUtils(collection)

        # Check
        output = db.get_words_from_date(date)
        self.assertEqual(output,expected,output)

