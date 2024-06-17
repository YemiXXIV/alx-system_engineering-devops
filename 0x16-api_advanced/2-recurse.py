#!/usr/bin/python3
"""
Recursive function to get all hot topics of a subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursive function that queries the Reddit API and returns a
    list containing
    the titles of all hot articles for a given subreddit.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "my bot 0.1"}
    params = {"after": after, "limit": 100}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        if response.status_code == 200:
            response_data = response.json()
            if 'data' in response_data and 'children' in response_data['data']:
                posts = response_data['data']['children']
                hot_list.extend([post['data']['title'] for post in posts])
                after = response_data['data']['after']
                if after:
                    return recurse(subreddit, hot_list, after)
                return hot_list
            else:
                return None
        else:
            return None
    except requests.RequestException:
        return None
    except ValueError:
        return None
