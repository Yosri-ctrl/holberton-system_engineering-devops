#!/usr/bin/python3
"""
export data in the JSON format
"""
import json
from requests import get
from sys import argv

if __name__ == "__main__":
    id = argv[1]
    list = []
    name = get(
        "http://jsonplaceholder.typicode.com/users/{}"
        .format(id)).json().get("username")
    tasks = get("http://jsonplaceholder.typicode.com/todos").json()

    for task in tasks:
        if (task.get("userId") == int(id)):
            temp = {}
            temp["task"] = task.get("title")
            temp["completed"] = task.get("completed")
            temp["username"] = name
            list.append(temp)

    with open("{}.json".format(id), 'w+') as jsonfile:
        json.dump({id: list}, jsonfile)
