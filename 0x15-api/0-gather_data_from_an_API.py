#!/usr/bin/python3
"""A script, using the API at https://jsonplaceholder.typicode.com to
return info about a given employee's TODO list progress.
"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    '''Set empty todo_list to collect todo items'''
    todo_list = []
    '''Users URL adds a new num to the path, which will be line arg 1'''
    users_url = 'https://jsonplaceholder.typicode.com/users/'
    user_id = argv[1]
    users_r = requests.get(users_url + user_id)
    user = users_r.json()
    '''Todos URL adds a new num to the path for each userId: line arg 1'''
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    todo_id = argv[1]
    todos_r = requests.get(todos_url + todo_id)
    todos = todos_r.json()
    if not user or not todos:
        print("Not a valid JSON")
    '''Search for 'completed' key, add 'title' of the todo to our todo_list'''
    for everything in todos:
        if everything.get('completed'):
            todo_list.append(everything.get('title'))
    '''Search for the 'name' key so we can display the employee's name'''
    for everything in todos:
        name = user.get('name')
    '''Count up the tasks collected in the todo_list with totals'''
    how_many_tasks = len(todo_list)
    total_tasks = len(todos)

    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), how_many_tasks, total_tasks))
    for everything in todo_list:
        print("\t" + everything)
'''
Example of executed script:
$ python3 0-gather_data_from_an_API.py 4
Employee Patricia Lebsack is done with tasks(6/20):
     odit optio omnis qui sunt
     doloremque aut dolores quidem fuga qui nulla
     sint amet quia totam corporis qui exercitationem commodi
     sequi dolorem sed
     eum ipsa maxime ut
     tempore molestias dolores rerum sequi voluptates ipsum consequatur
'''
