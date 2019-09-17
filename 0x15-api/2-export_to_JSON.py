#!/usr/bin/python3
"""A script, using the API at https://jsonplaceholder.typicode.com to
return info about a given employee's TODO list progress, converted to json
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
    username = user.get('username')
    '''Todos URL adds a new num to the path for each userId: line arg 1'''
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    todo_id = argv[1]
    todos_r = requests.get(todos_url + todo_id)
    todos = todos_r.json()

    if not user or not todos:
        print("Not a valid JSON")

    json_file = argv[1] + ".json"
    dict = {}
    list = []
    json_dictionary = {}

    '''Search for 'completed' key, add 'title' of the todo to our todo_list'''
    for everything in todos:
        completed = everything.get('completed')
        title = everything.get('title')
        dict.update(
            {"task": title, "completed": completed, "username": username})
        list.append(dict)
        json_dictionary = argv[1]

        with open(json_file, mode="w") as output:
            json.dump(json_dictionary, output)
'''
Execute script:
$ python3 2-export_to_JSON.py 2
vagrant@ubuntu$ cat 2.json
'''
