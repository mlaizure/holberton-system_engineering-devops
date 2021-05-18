#!/usr/bin/python3
"""queries Reddit API"""


def top_ten(subreddit):
    """prints titles of first 10 hot posts for a given subreddit"""
    import requests

    url = 'https://api.reddit.com/r/{}/hot?limit=10'.format(subreddit)

    sub_info = requests.get(url,
                            headers={"user-agent": "user"},
                            allow_redirects=False).json()

    if 'data' in sub_info:
        for post in sub_info['data']['children']:
            print(post['data']['title'])
    else:
        print('None')
