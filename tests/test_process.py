# -*- coding: utf-8 -*-

from .context import textprocessor

import unittest


class ProcessTestSuite(unittest.TestCase):
    """Test cases for text processor general function"""

    def test_simple_word(self):
        """Simple single word test"""
        text = "test"
        expected = [['test', 1]]

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_multiple_word(self):
        """Simple multiple words test"""
        text = "test portatil portatil cabra"
        expected = [['test', 1], ['cabra',1], ['portatil',2]]

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_valid_and_punctuation(self):
        """Valid words mixed with punctuation test"""
        text = " ,alguna .. ordenador  () lista ## hashtag #"
        expected = [['ordenador',1], ['alguna',1], ['lista',1], ['hashtag',1] ]

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")


    def test_valid_and_stop_words(self):
        """Valid words mixed with stop words test"""
        text = " alguna estar ordenador tengamos lista hashtag otro"
        expected = [['ordenador',1], ['alguna',1], ['lista',1], ['hashtag',1] ]

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_valid_and_stop_words_and_punctuation(self):
        """Valid words mixed with punctuation and stop words test"""
        text = " alguna.. ,estar -- + ordenador  () () = tengamos ' ¡ lista @# hashtag otro"
        expected = [['ordenador',1], ['alguna',1], ['lista',1], ['hashtag',1] ]

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_multiple_word_uppsercase(self):
        """Multiple words with uppercase test"""
        text = "TEST PORtatIl porTatIl caBra"
        expected = [['test', 1], ['cabra',1], ['portatil',2]]

    def test_valid_uppercase_and_stop_words_and_punctuation(self):
        """Valid words with uppercase mixed with punctuation and stop words test"""
        text = " ALguna.. ,esTAr -- + ORdEnAdor  () () = tengaMoS ' ¡ LISTA @# HAsHtAg otro"
        expected = [['ordenador',1], ['alguna',1], ['lista',1], ['hashtag',1] ]

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_empty(self):
        """Empty text test"""
        text = ""
        expected = []

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_invalid_number(self):
        """Number input test"""
        text = 10
        expected = TypeError

        with self.assertRaises(expected) as cm:
            textprocessor.process(text)
        self.assertEqual('Text must be a valid string', str(cm.exception), "No exception raised")

    def test_only_stop_words(self):
        """only stop words test"""
        text = ""
        expected = []

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_only_punctuation(self):
        """only punctuation test"""
        text = " ,. - ^=) ,. ~~~ #"
        expected = []

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    def test_only_punctuation_and_stop_words(self):
        """only punctuation and stop words test"""
        text = " ,son ..tengamos = sentidos ))(nuestra#"
        expected = []

        res = textprocessor.process(text)
        self.assertListEqual(res, expected, "Unexpected output")

    
    

if __name__ == '__main__':
    unittest.main()
