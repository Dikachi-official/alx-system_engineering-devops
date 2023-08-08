#!/usr/bin/python3
"""
Query Reddit API to find top 10 hot posts of a given subreddit
"""
import requests


def top_ten(subreddit):
    """
    Prints the titles of first 10 hot posts for a given subreddit

    Args:
        subreddit (str): Subreddit name to query Reddit API
    """
    headers = {'User-Agent': 'Holberton Student 329'}
    check_url = 'https://reddit.com/api/search_reddit_names.json'
    params = {'query': subreddit, 'exact': True}
    check = requests.get(check_url, headers=headers, params=params)
    if check.status_code != 200 or len(check.json()['names']) is 0:
        print(None)
        return
    url = 'https://reddit.com/r/{}/hot/.json'.format(subreddit)
    sr = requests.get(url, headers=headers)
    hot_posts = sr.json().get('data').get('children')
    i = 0
    while i < len(hot_posts) and i < 10:
        print(hot_posts[i].get('data').get('title'))
        i += 1
