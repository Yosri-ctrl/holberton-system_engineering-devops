#!/usr/bin/python3
"""
Using what you did in the task #0,
extend your Python script to export data in the JSON format.
"""
import json
from requests import get

if __name__ == "__main__":
    users = get("http://jsonplaceholder.typicode.com/users").json()
    tasks = get("http://jsonplaceholder.typicode.com/todos").json()
    storage = {}

    for user in users:
        id = user.get("id")
        name = user.get("username")
        list = []

        for task in tasks:
            if (task.get("userId") == id and
                    str(task.get("completed")) == "True"):
                temp = {}
                temp["task"] = task.get("title")
                temp["completed"] = task.get("completed")
                temp["username"] = name
                list.append(temp)
        storage[id] = list

    with open("todo_all_employees.json", 'w+') as jsonfile:
        json.dump(storage, jsonfile)
