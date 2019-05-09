#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import requests


def top_ten(subreddit):
    """
    Prints the top ten 'hot' posts for a subreddit.
    """

    headers = {'User-agent': 'Wescott'}

    base = 'https://www.reddit.com/'
    query = '/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(base + query, headers=headers)
    response.raise_for_status()
    top = response.json().get('data', {}).get('children', [])
    if not top:
        print(None)
    for post in top:
        print(post.get('data').get('title'))
