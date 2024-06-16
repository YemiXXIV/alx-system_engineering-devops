#!/usr/bin/python3
"""
get the top ten hot topics of a subreddit
"""
import requests


def top_ten(subreddit):
    """
    get the top ten hot topics of a subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "my bot 0.1"}

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        if response.status_code == 200:
            response_data = response.json()
            titles = response_data['data']['children']
            for title in titles:
                print(title['data']['title'])
        else:
            print(None)
    except requests.RequestException as e:
        print(None)
    except ValueError:
        print(None)
