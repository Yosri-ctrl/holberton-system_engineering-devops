#!/usr/bin/python3
""" return the top ten posts """
import requests


def top_ten(subreddit):
    """ return the most hot posts """
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    head = {'user-agent': 'Yureickane'}
    req = requests.get(url, headers=head)
    if (req.status_code is 302 or req.status_code is 404):
        print("None")
    elif 'data' not in req.json():
        print("None")
    else:
        req = req.json()
        for post in req['data']['children']:
            print(post['data']['title'])
