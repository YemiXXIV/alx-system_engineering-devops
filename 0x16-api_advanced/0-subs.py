#!/usr/bin/python3
"""
Function that queries subscribers on a given Reddit subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """
    Return the number of subscribers on a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "my bot 0.1"
    }

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            response_data = response.json()
            if 'data' in response_data and 'subscribers' in response_data['data']:
                return response_data['data']['subscribers']
            else:
                return 0
        else:
            return 0
    except requests.RequestException:
        return 0
    except ValueError:
        return 0
