#!/usr/bin/python3
""" Return how many subrscribers to this user """
import requests


def number_of_subscribers(subreddit):
    """return the number of subscribers"""
    url = "http://www.reddit.com/r/{}/about.json".format(subreddit)
    head = {'user-agent': 'Yureickane'}
    req = requests.get(url, headers=head)
    if (req.status_code is 302 or req.status_code is 404):
        return 0
    req = req.json()
    if ('error' in req):
        return 0
    elif ('subscribers' in req['data']):
        return req['data']['subscribers']
    else:
        return 0
