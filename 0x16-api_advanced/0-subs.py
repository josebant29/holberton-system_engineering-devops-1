#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import requests
import sys


def number_of_subscribers(subreddit):
    """
    Returns the number of subs for a given subreddit.
    """

    headers = {'User-agent': 'Wescott'}

    base = 'https://www.reddit.com/'
    query = '/r/{}/about.json'.format(subreddit)
    response = requests.get(base + query, headers=headers)
    response.raise_for_status()
    subs = response.json().get('data', {}).get('subscribers')
    if not subs:
        return 0
    return subs


if __name__ == '__main__':
    print(number_of_subscribers('showerthoughts'))
