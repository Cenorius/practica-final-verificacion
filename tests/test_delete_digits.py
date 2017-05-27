# -*- coding: utf-8 -*-

from .context import textprocessor

import unittest


class DeleteDigitsTestSuite(unittest.TestCase):
    """Test cases for Delete Punctuation Signs"""

    def test_clean_string(self):
        """Test delete digits in a clean string"""
        string = "this is a clean string"
        expected = "this is a clean string"

        res = textprocessor.remove_digits(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_clean_unicode_string(self):
        """Test delete digits in a clean unicode string"""
        string = u'this is a clean string'
        expected = "this is a clean string"

        res = textprocessor.remove_digits(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_dirty_string(self):
        """Test delete digits in a dirty string"""
        string = "This 1is 2 a 3cle3an 4st5ri67901392ng"
        expected = "This is  a clean string"

        res = textprocessor.remove_digits(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_dirty_unicode_string(self):
        """Test delete digits in a dirty unicode string"""
        string = u'This 1is 2 a 3cle3an 4st5ri67901392ng'
        expected = "This is  a clean string"

        res = textprocessor.remove_digits(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_all_numbers_string(self):
        """Test delete digits in a all-numbers string"""
        string = "1239612451526981237124612"
        expected = ""

        res = textprocessor.remove_digits(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_all_numbers_unicode_string(self):
        """Test delete digits in a all-numbers unicode string"""
        string = u'1239612451526981237124612'
        expected = ""

        res = textprocessor.remove_digits(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_empty_string(self):
        """Test with an empty string"""
        string = ""
        expected = ""

        res = textprocessor.remove_digits(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_invalid_input_number(self):
        """Test with digits"""

        string = 12323
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.remove_digits(string)
        self.assertEqual('Argument is not a string',str(cm.exception),"No exception raised")


if __name__ == '__main__':
    unittest.main()
