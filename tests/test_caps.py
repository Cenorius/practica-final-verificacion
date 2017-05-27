# -*- coding: utf-8 -*-

from .context import textprocessor

import unittest


class DeleteDigitsTestSuite(unittest.TestCase):
    """Test cases for Delete Punctuation Signs"""

    def test_clean_string(self):
        """Test clean string"""
        string = "this is a clean string"
        expected = "this is a clean string"

        res = textprocessor.convert_caps(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_caps_string(self):
        """Test all caps string"""
        string = "THIS IS A STRING"
        expected = "this is a string"

        res = textprocessor.convert_caps(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_caps_unicode_string(self):
        """Test all caps unicode string"""
        string = u"THIS IS A STRING"
        expected = "this is a string"

        res = textprocessor.convert_caps(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_clean_unicode_string(self):
        """Test clean unicode string"""
        string = u'this is a clean string'
        expected = "this is a clean string"

        res = textprocessor.convert_caps(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_mix_upper_and_lower_string(self):
        """Test mix upper and lower string"""
        string = 'ThIs iS A cLeaN sTring'
        expected = "this is a clean string"

        res = textprocessor.convert_caps(string)
        self.assertEqual(res, expected, "Strings do not match")


if __name__ == '__main__':
    unittest.main()
