"""Unit test api_client module"""
import json
import os.path
import unittest

import requests

from capio_word_exporter import api_client

# pylint: disable=invalid-name


def _get_expected_result(t_id):
    """Load transcript expected result stored as JSON file in this dir"""
    this_dir = os.path.dirname(__file__)
    path = os.path.join(this_dir, '%s.json' % t_id)
    with open(path, 'r') as file_:
        return json.load(file_)


class APIClientTest(unittest.TestCase):
    """Test functions related to API call"""
    def test_fetch_transcript(self):
        """fetch_transcript fetches the correct response"""
        api_key = '262ac9a0c9ba4d179aad4c0b9b02120a'
        t_id = '593f237fbcae700012ba8fcd'
        found = api_client.fetch_transcript(t_id, api_key)
        expected = _get_expected_result(t_id)
        self.assertEqual(found, expected)

    def test_fetch_transcript_unauthorized(self):
        """fetch_transcript raises 401 unauthorized error for invalid API Key"""
        api_key = 'invalid_random_api_key'
        t_id = '593f237fbcae700012ba8fcd'
        with self.assertRaises(requests.exceptions.HTTPError) as caught:
            api_client.fetch_transcript(t_id, api_key)
        error = caught.exception
        self.assertEqual(error.response.status_code, 401)

    def test_fetch_transcript_unexisting(self):
        """fetch_transcript raises 500 unauthorized error for invalid API Key"""
        api_key = '262ac9a0c9ba4d179aad4c0b9b02120a'
        t_id = 'invalid_random_transcript_id'
        with self.assertRaises(requests.exceptions.HTTPError) as caught:
            api_client.fetch_transcript(t_id, api_key)
        error = caught.exception
        self.assertEqual(error.response.status_code, 500)
