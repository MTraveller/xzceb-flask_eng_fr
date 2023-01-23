""" Tests for translator.py """

import unittest

from translator import english_to_french, french_to_english


class TestEnglishToFrench(unittest.TestCase):
    """ Class to test text from english to french """

    def test_null_english_to_french(self):
        """ Function to test against input of null """
        with self.assertRaises(ValueError):
            english_to_french(None)

    def test_word_hello_to_bonjour(self):
        """ Function to test translation from
            english to french """
        self.assertEqual(english_to_french("Hello"), "Bonjour")


class TestFrenchToEnglish(unittest.TestCase):
    """ Class to test text from french to english """

    def test_null_french_to_english(self):
        """ Function to test against input of null """
        with self.assertRaises(ValueError):
            french_to_english(None)

    def test_word_bonjour_to_hello(self):
        """ Function to test translation from
            french to english """
        self.assertEqual(french_to_english("Bonjour"), "Hello")


unittest.main()
