#!/usr/bin/python3
"""
module to return the number of subscribers for a subreddit
"""
import requests


def number_of_subscribers(subreddit):
    """
    number of subscribers for a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {'User-Agent': 'Mozilla/5.0'}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            data = response.json()
            subscribers = data['data']['subscribers']
            return subscribers
        else:
            return 0
    except requests.RequestException as e:
        return 0
