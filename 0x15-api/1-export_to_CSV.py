#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import csv
import requests
import sys


def get_employee_name(e_id):
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(e_id)
    user = requests.get(user_url)
    user.raise_for_status()
    name = user.json().get('name')
    return name


def get_employee_username(e_id):
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(e_id)
    user = requests.get(user_url)
    user.raise_for_status()
    username = user.json().get('username')
    return username


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


def export_to_csv(filename, e_id, name, tasks):
    filename = filename + '.csv'
    with open(filename, 'w') as f:
        fieldnames = [
            'e_id',
            'name',
            'completed',
            'title']
        writer = csv.DictWriter(
            f,
            quoting=csv.QUOTE_ALL,
            fieldnames=fieldnames)
        for task in tasks:
            if task.get('userId') == e_id:
                writer.writerow({
                    'title': task.get('title'),
                    'completed': task.get('completed'),
                    'name': name,
                    'e_id': e_id})


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    employee_username = get_employee_username(employee_id)
    employee_tasks = get_employee_tasks(employee_id)
    export_to_csv(sys.argv[1], employee_id, employee_username, employee_tasks)
