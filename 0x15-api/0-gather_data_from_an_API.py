#!/usr/bin/python3
"""
returns information about his/her TODO list progress
"""
from sys import argv
from requests import get


if __name__ == "__main__":
    try:
        id = argv[1]
    
        nbr_tasks = 0
        tasks_completed = []

        name = get("https://jsonplaceholder.typicode.com/users/{}".
        format(id)).json().get("name")
        tasks = get("http://jsonplaceholder.typicode.com/todos").json()

        for task in tasks:
            if (task.get("userId") == int(id)):
                if str(task.get("completed")) == "True":
                    tasks_completed.append(task)
                nbr_tasks += 1

        print("{} is done with tasks({}/{}):".format(name,
                                                    len(tasks_completed),
                                                    nbr_tasks))
        for i in tasks_completed:
            print("\t {}".format(i.get("title")))
    except:
        pass
