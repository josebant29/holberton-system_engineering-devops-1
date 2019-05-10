#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Prints the top ten 'hot' posts for a subreddit.
    """

    headers = {'User-agent': 'Wescott'}

    base = 'https://www.reddit.com/'
    query = '/r/{}/hot.json?after={}'.format(subreddit, after)
    response = requests.get(base + query, headers=headers)
    top = response.json().get('data', {}).get('children', [])
    after = response.json().get('data', {}).get('after', None)
    if response != 200:
        return None
    if not after:
        return hot_list
    for post in top:
        hot_list.append(post.get('data').get('title'))
    return recurse(subreddit, hot_list=hot_list, after=after)
