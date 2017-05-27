# -*- coding: utf-8 -*-

from .context import textprocessor

import unittest


class DeletePunctuationSignsTestSuite(unittest.TestCase):
    """Test cases for Delete Punctuation Signs"""

    def test_clean_string(self):
        """Test delete punctuation signs in a clean string"""
        string = "this is a clean string"
        expected = ["this", "is", "a", "clean", "string"]

        res = textprocessor.remove_punctuation(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_clean_unicode_string(self):
        """Test delete punctuation signs in a clean unicode string"""
        string = u'this is a clean string'
        expected = ["this", "is", "a", "clean", "string"]

        res = textprocessor.remove_punctuation(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_dirty_string(self):
        """Test delete punctuation signs in a dirty string"""
        string = "¡Hola! No. SE. és,cri,bir.Vayä.Pta.bida.,!"
        expected = ["Hola", "No", "SE", "es", "cri", "bir", "Vaya", "Pta", "bida"]

        res = textprocessor.remove_punctuation(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_dirty_unicode_string(self):
        """Test delete punctuation signs in a dirty unicode string"""
        string = u'¡Hola! No. SE. és,cri,bir.Vayä.Pta.bida.,!'
        expected = ["Hola", "No", "SE", "es", "cri", "bir", "Vaya", "Pta", "bida"]

        res = textprocessor.remove_punctuation(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_all_signs_string(self):
        """Test delete punctuation signs in a all-signs string"""
        string = "&%=)!&·)%=&%!)&) (&·/!%!&"
        expected = []

        res = textprocessor.remove_punctuation(string)
        self.assertListEqual(res, expected, "Lists do not match")

    def test_empty_string(self):
        """Test with an empty string"""
        string = ""
        expected = []

        res = textprocessor.remove_punctuation(string)
        self.assertEqual(res, expected, "Strings do not match")

    def test_invalid_input_number(self):
        """Test with digits"""

        string = 12323
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.remove_digits(string)
        self.assertEqual('Argument is not a string',str(cm.exception), "No exception raised")


if __name__ == '__main__':
    unittest.main()
