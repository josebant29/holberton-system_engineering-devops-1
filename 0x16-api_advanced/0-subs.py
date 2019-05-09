#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Returns the number of subs for a given subreddit.
    """

    headers = {'User-agent': 'Wescott'}

    base = 'https://www.reddit.com/'
    query = '/r/{}/about.json'.format(subreddit)
    response = requests.get(base + query, headers=headers)
    subs = response.json().get('data', {}).get('subscribers')
    if not subs:
        return 0
    return subs
