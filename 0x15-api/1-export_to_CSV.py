#!/usr/bin/python3
"""A script, using the API at https://jsonplaceholder.typicode.com to
return info about a given employee's TODO list progress, exported to CSV
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
    user_name = user.get('username')
    '''Todos URL adds a new num to the path for each userId: line arg 1'''
    todos_url = 'https://jsonplaceholder.typicode.com/todos?userId='
    todo_id = argv[1]
    todos_r = requests.get(todos_url + todo_id)
    todos = todos_r.json()

    csv = user_id + ".csv"
    '''Search for 'completed' key, add 'title' of the todo to our todo_list'''
    for everything in todos:
        completed = everything.get('completed')
        title = everything.get('title')
        with open(csv, "a+") as output:
            output.write('"{}","{}", "{}", "{}"\n'.format
                         (user_id, user_name, completed, title))
    for everything in todo_list:
        print("\t" + everything)
'''
Sample of executed script:
$ python3 1-export_to_CSV.py 2
sylvain@ubuntu$ cat 2.csv
"2","Antonette","False","suscipit repellat esse quibusdam voluptatem incidunt"
"2","Antonette","True","distinctio vitae autem nihil ut molestias quo"
"2","Antonette","False","totam quia non"
"2","Antonette","True","totam atque quo nesciunt"
'''
