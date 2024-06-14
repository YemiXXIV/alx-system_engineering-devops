#!/usr/bin/python3
"""
module to return the number of subscribers for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers for a subreddit
    """
    result = requests.get(
        f"https://www.reddit.com/r/{subreddit}/about.json",
        headers={'User-agent': 'my bot 0.1'})

    if result.status_code == 200:
        response_data = result.json()
        subscribers = response_data['data']['subscribers']
        return subscribers
    else:
        return 0
