#!/usr/bin/python3
"""
Returns info for a given employee using API.
"""

import csv
import json
import requests


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
            writer.writerow({
                'title': task.get('title'),
                'completed': task.get('completed'),
                'name': name,
                'e_id': e_id})


def format_user_data(e_id, name, tasks):
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
    return wrapper


def export_to_json(filename, wrapper):
    filename = filename + '.json'
    with open(filename, 'w') as f:
        json.dump(wrapper, f)


def export_all_employee_data(filename):
    wrapper = {}
    users_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(users_url)
    users.raise_for_status()
    for user in users.json():
        e_id = user.get('id')
        username = user.get('username')
        tasks = get_employee_tasks(e_id)
        user_data = format_user_data(e_id, username, tasks)
        wrapper[str(e_id)] = user_data[str(e_id)]
    export_to_json(filename, wrapper)


if __name__ == '__main__':
    export_all_employee_data('todo_all_employees')
