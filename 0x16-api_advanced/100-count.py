#!/usr/bin/python3
"""queries Reddit API"""


def count_words(subreddit, word_list, after=None, counts={}):
    """prints count of keywords in hot article titles for given subreddit"""
    import requests

    if not after:
        url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    else:
        url = 'https://api.reddit.com/r/{}/hot?after={}'.format(
            subreddit, after)

    sub_info = requests.get(url,
                            headers={"user-agent": "user"},
                            allow_redirects=False)

    try:
        sub_info = sub_info.json()
    except:
        return None

    if 'data' not in sub_info:
        return None

    for post in sub_info['data']['children']:
        for word in post['data']['title'].split():
            for key_word in word_list:
                if key_word.lower() == word.lower():
                    if key_word.lower() in counts.keys():
                        counts[key_word.lower()] += 1
                    else:
                        counts[key_word.lower()] = 1

    after = sub_info['data']['after']

    if after:
        return count_words(subreddit, word_list, after, counts)

    for key in sorted(counts, key=counts.get, reverse=True):
        print('{}: {}'.format(key, counts[key]))
