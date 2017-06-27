"""Unit test parser module"""
import unittest

from capio_word_exporter import parser

# pylint: disable=protected-access


class APIClientTest(unittest.TestCase):
    """Test functions related to API call"""
    def test_parse_words(self):
        """_parse_words extract words and color for low confidence"""
        words = [
            {
                'word': 'foo',
                'confidence': 1.0,
            },
            {
                'word': 'bar',
                'confidence': 0.5,
            },
            {
                'word': 'foo',
                'confidence': 0.8,
            },
        ]
        found = parser._parse_words(words)
        expected = [
            {
                'word': 'foo',
            },
            {
                'word': 'bar',
                'color': (255, 0, 0),
            },
            {
                'word': 'foo',
            },
        ]
        self.assertEqual(found, expected)
