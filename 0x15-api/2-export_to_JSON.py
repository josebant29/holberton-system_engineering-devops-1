#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import csv
import json
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


def export_to_csv(e_id, name, tasks):
    filename = sys.argv[1] + '.csv'
    with open(filename, 'w') as f:
        fieldnames = [
            'e_id',
            'name',
            'completed',
            'title']
        writer = csv.DictWriter(f, quoting=csv.QUOTE_ALL, fieldnames=fieldnames)
        for task in tasks:
            writer.writerow({
                'title': task.get('title'),
                'completed': task.get('completed'),
                'name': name,
                'e_id': e_id})

def export_to_json(e_id, name, tasks):
    wrapper = {}
    user_data = []
    for task in tasks:
        task_data = {
            'task': task.get('title'),
            'completed': task.get('completed'),
            'username': name
        }
        user_data.append(task_data)
    wrapper[str(e_id)] = user_data
    filename = sys.argv[1] + '.json'
    with open(filename, 'w') as f:
        json.dump(wrapper, f)


if __name__ == '__main__':
    employee_id = int(sys.argv[1])
    employee_name = get_employee_name(employee_id)
    employee_tasks = get_employee_tasks(employee_id)
    export_to_json(employee_id, employee_name, employee_tasks)
