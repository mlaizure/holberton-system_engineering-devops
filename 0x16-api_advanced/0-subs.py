#!/usr/bin/python3
"""function that queries Reddit API"""


def number_of_subscribers(subreddit):
    """queries Reddit API and returns number of subscribers"""
    import requests

    url = 'https://api.reddit.com/r/{}/about/'.format(subreddit)

    sub_info = requests.get(url,
                            headers={"user-agent" : "user"},
                            allow_redirects=False).json()

    if 'data' in sub_info:
        return sub_info['data']['subscribers']
    return 0
