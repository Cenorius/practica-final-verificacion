# -*- coding: utf-8 -*-

from .context import textprocessor

import unittest


class StopWordsTestSuite(unittest.TestCase):
    """Test cases for Stop words"""

    def test_no_stop_words(self):
        """Test without stop words"""
        string = ["aaaa", u'ameba', "ordenador"]
        expected = ["aaaa", "ameba", "ordenador"]

        res = textprocessor.remove_stop_words(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_empty(self):
        """Test empty array"""
        string = []
        expected = []

        res = textprocessor.remove_stop_words(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_mixed_types(self):
        """Test with mixed values"""
        string = ["aaaa", True]
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.remove_stop_words(string)
        self.assertEqual('Argument in list is not a string', str(cm.exception), "No exception raised")

    def test_without_list(self):
        """Test with incorrect value"""
        string = 4
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.remove_stop_words(string)
        self.assertEqual('Argument is not a list', str(cm.exception), "No exception raised")

    def test_with_all_stop_words(self):
        """Test with all stop words"""
        string = ["tienen", u'a', u'somos', "tengan"]
        expected = []

        res = textprocessor.remove_stop_words(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_with_some_stop_words(self):
        """Test with some stop words"""
        string = ["patata", "ameba", "tienen", "a", "tacata", "somos", "tengan", "mamasita"]
        expected = ["patata", "ameba", "tacata", "mamasita"]

        res = textprocessor.remove_stop_words(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_uppercase(self):
        """Test with uppercase letters"""
        string = ["PATATA", "AMEBA", "TIENEN", "A", "TACATA", "SOMOS", "TENGAN", "MAMASITA"]
        expected = ["patata", "ameba", "tacata", "mamasita"]

        res = textprocessor.remove_stop_words(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_mixed_uppercase(self):
        """Test with uppercase letters"""
        string = ["PatAtA", "AmEbA", "tiENEn", "a", "TaCAtA", "SoMOS", "TeNgAN", "MaMasITA"]
        expected = ["patata", "ameba", "tacata", "mamasita"]

        res = textprocessor.remove_stop_words(string)
        self.assertListEqual(res, expected, "Lists do not match")

if __name__ == '__main__':
    unittest.main()
