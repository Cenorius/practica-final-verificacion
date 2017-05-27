# -*- coding: utf-8 -*-

from .context import textprocessor

import unittest


class SortbyTimesTestSuite(unittest.TestCase):
    """Test cases for Delete Punctuation Signs"""

    def test_one_time_each_word(self):
        """Test repetition of one word at a time"""
        string = ["this", "is", u'a', "clean", u'string']
        expected = [['this', 1], ['a', 1], ['is', 1], ['string', 1], ['clean', 1]]

        res = textprocessor.sort_by_times(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_two_times_some_words(self):
        """Test with some words repeated"""
        string = ["this", "this", "is", "a", "clean", "string", "a"]
        expected = [['is', 1], ['string', 1], ['clean', 1], ['this', 2], ['a', 2]]

        res = textprocessor.sort_by_times(string)
        print res
        self.assertListEqual(res, expected, "Lists do not match")

    def test_empty(self):
        """Test with empty list"""
        string = []
        expected = []

        res = textprocessor.sort_by_times(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_with_True(self):
        """Test with True value"""
        string = [True]
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.sort_by_times(string)
        self.assertEqual('Argument in list is not a string',str(cm.exception), "No exception raised")

    def test_with_mixed_types_list(self):
        """Test with mixed values"""
        string = ["aaaa", True]
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.sort_by_times(string)
        self.assertEqual('Argument in list is not a string', str(cm.exception), "No exception raised")

    def test_without_list(self):
        """Test with incorrect value"""
        string = 4
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.sort_by_times(string)
        self.assertEqual('Argument is not a list',str(cm.exception), "No exception raised")


if __name__ == '__main__':
    unittest.main()
