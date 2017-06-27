"""Module for making API call to Capio API"""
import logging

import requests

_LG = logging.getLogger(__name__)
_BASE_URL = 'https://api.capio.ai/v1'


def fetch_transcript(t_id, api_key):
    """Fetch speech transcript data from Capio API

    Parameters
    ----------
    t_id : str
        Transcript ID
    api_key : str
        API Key

    Returns
    -------
    JSON object
    """
    route = 'speech/transcript/{}'.format(t_id)
    url = '{}/{}'.format(_BASE_URL, route)
    headers = {'apiKey': api_key}
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
