#!/usr/bin/python3
"""queries Reddit API"""


def recurse(subreddit, hot_list=[], after=None):
    """makes list of all hot posts for a given subreddit"""
    import requests

    if not after:
        url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    else:
        url = 'https://api.reddit.com/r/{}/hot?after={}'.format(
            subreddit, after)

    sub_info = requests.get(url,
                            headers={"user-agent": "user"},
                            allow_redirects=False).json()

    if 'data' not in sub_info:
        return None

    for post in sub_info['data']['children']:
        hot_list.append(post['data']['title'])
    after = sub_info['data']['after']

    if after:
        return recurse(subreddit, hot_list, after)
    return hot_list
