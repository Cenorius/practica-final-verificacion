# -*- coding: utf-8 -*-

from .context import DBUtils

import unittest

class FormatWordsTestSuite(unittest.TestCase):
    def test_is_date(self):

        date="1/2/1000"

        # Get DBUtils
        db = DBUtils.DBUtils(None)

        result=db._is_date(date)

        self.assertTrue(result)

    def test_not_date(self):

        date="1/2/1"

        # Get DBUtils
        db = DBUtils.DBUtils(None)

        result=db._is_date(date)

        self.assertFalse(result)

    def test_not_str(self):

        date=1

        # Get DBUtils
        db = DBUtils.DBUtils(None)

        result=db._is_date(date)

        self.assertFalse(result)
        