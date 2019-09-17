#!/usr/bin/python3
"""A script, using the API at https://jsonplaceholder.typicode.com to
return info about a given employee's TODO list progress.
"""
import requests
import json


url = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(
    url,
    params ={"userId": 1}
)
todos = response.json()
print(todos)
print(response.url)

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
