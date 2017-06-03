# -*- coding: utf-8 -*-

from .context import DBUtils

import mock
import unittest
from test_auxiliary_functions import get_fake_collection

class InsertWordsTestSuite(unittest.TestCase):
      def test_not_exists_in_database(self):

        words = [["mal",7],["bien",6]]
        date="1/2/3"
        title="title"

        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        db._format_words = mock.MagicMock(return_value=[{"word":"mal","count":7},{"word":"bien","count":6}])
        # Force existance
        db.exists_article_in_db = mock.MagicMock(return_value=False)
        db._is_date = mock.MagicMock(return_value=True)

        result=db.insert_words(date,title,words)

        self.assertTrue(result)

      def test_exists_in_database(self):

        words = [["mal",7],["bien",6]]
        date="1/2/3"
        title="title"

        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        db._format_words = mock.MagicMock(return_value=[{"word":"mal","count":7},{"word":"bien","count":6}])
        # Force existance
        db.exists_article_in_db = mock.MagicMock(return_value=True)
        db._is_date = mock.MagicMock(return_value=True)

        result=db.insert_words(date,title,words)

        self.assertFalse(result)

      def test_date_not_str(self):

        words = [["mal",7],["bien",6]]
        date=1
        title="title"

        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        with self.assertRaises(Exception) as cm:
            db.insert_words(date,title,words)
        self.assertEqual("Date format is not valid", str(cm.exception), "No exception 'Date format is not valid' raised")


      def test_title_not_str(self):

        words = [["mal",7],["bien",6]]
        date="1/2/3"
        title=1

        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        with self.assertRaises(TypeError):
          db.insert_words(date,title,words)


      def test_words_not_list(self):

        words = "list"
        date="1/2/3"
        title="title"

        collection = get_fake_collection()

        # Get DBUtils
        db = DBUtils.DBUtils(collection)

        with self.assertRaises(TypeError):
          db.insert_words(date,title,words)

      def test_words_date_format_incorrect_in_database(self):

        words = [["mal",7],["bien",6]]
        date="1667"
        title="title"

        collection = get_fake_collection()
        
        # Get DBUtils
        db = DBUtils.DBUtils(collection)
        
        with self.assertRaises(Exception) as cm:
            db.insert_words(date,title,words)
        self.assertEqual("Date format is not valid", str(cm.exception), "No exception 'Date format is not valid' raised")