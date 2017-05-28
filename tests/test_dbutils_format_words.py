# -*- coding: utf-8 -*-

from .context import DBUtils

import unittest

class FormatWordsTestSuite(unittest.TestCase):
      def test_format_words(self):

        words = [["mal",7],["bien",6]]
        expected = [{"word":"mal","count":7},{"word":"bien","count":6}]
        
        # Get DBUtils
        db = DBUtils.DBUtils(None)

        result=db._format_words(words)

        self.assertEqual(result,expected,result)