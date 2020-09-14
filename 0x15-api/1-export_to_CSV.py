#!/usr/bin/python3
"""
export data in the CSV format
"""
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    id = argv[1]

    name = get(
        "https://jsonplaceholder.typicode.com/users/{}"
        .format(id)).json().get("name")
    tasks = get("http://jsonplaceholder.typicode.com/todos").json()

    with open("{}.csv".format(id), "a") as csvfile:
        for task in tasks:
            if task.get('userId') == int(id):
                csvfile.write('"{}","{}","{}","{}"\n'.format(
                    id,
                    name,
                    task.get("completed"),
                    task.get("title")))
