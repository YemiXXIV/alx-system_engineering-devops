#!/usr/bin/python3
"""
Get the top ten hot topics of a subreddit.
"""
import requests


def top_ten(subreddit):
    """
    Get the top ten hot topics of a subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {"User-Agent": "my bot 0.1"}

    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            response_data = response.json()
            if 'data' in response_data and 'children' in response_data['data']:
                titles = response_data['data']['children']
                for title in titles:
                    print(title['data']['title'])
            else:
                print(None)
        else:
            print(None)
    except requests.RequestException:
        print(None)
    except ValueError:
        print(None)
