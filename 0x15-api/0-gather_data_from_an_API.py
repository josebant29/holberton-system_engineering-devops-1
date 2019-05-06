#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import sys

import requests


def get_employee_name(e_id):
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(e_id)
    user = requests.get(user_url)
    user.raise_for_status()
    name = user.json().get('name')
    return name


def get_employee_tasks(e_id):
    payload = 'userId={}'.format(e_id)
    tasks_url = 'https://jsonplaceholder.typicode.com/todos?'
    tasks = requests.get(tasks_url + payload)
    tasks.raise_for_status()
    return tasks.json()


def print_employee_data(name, tasks):
    complete_tasks = 0
    total_tasks = 0
    task_titles = []
    for task in tasks:
        if task.get('completed'):
            complete_tasks += 1
            task_titles.append(task.get('title'))
        total_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(
        name,
        complete_tasks,
        total_tasks))
    for title in task_titles:
        print('\t {}'.format(title))


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    employee_name = get_employee_name(employee_id)
    employee_tasks = get_employee_tasks(employee_id)
    print_employee_data(employee_name, employee_tasks)
