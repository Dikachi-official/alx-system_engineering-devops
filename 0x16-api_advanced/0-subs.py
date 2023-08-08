#!/usr/bin/python3
"""
Query Reddit API to find number of subscribers of a given subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    Args:
        subreddit (str): Subreddit name to query Reddit API

    Return:
        subs (int): number of subscribers, 0 if not a valid subreddit
    """
    headers = {'User-Agent': 'Holberton Student 329'}
    url = 'https://reddit.com/r/{}/about.json'.format(subreddit)
    sr = requests.get(url, headers=headers)
    if sr.status_code != 200:
        return 0
    subs = sr.json().get('data').get('subscribers')
    return subs
