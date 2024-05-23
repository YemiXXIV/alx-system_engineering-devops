#!/usr/bin/python3
"""
This script returns the to-do list information of a given
employee ID and exports the data to a JSON file.

The script takes a command-line argument and fetches the
corresponding data and to-do list from the provided API, then
prints the tasks completed by the employee and exports all tasks
to a JSON file.
"""

import json
import requests
import sys


if __name__ == "__main__":
    url_api = "https://jsonplaceholder.typicode.com/"

    # To get employee information using the employee ID
    employee_id = sys.argv[1]
    employee = requests.get(url_api + "users/{}".format(employee_id)).json()

    # To get to-do list for the employee using the employee ID
    values = {"userId": employee_id}
    todo_list = requests.get(url_api + "todos", params=values).json()

    completed = [
        a.get("title") for a in todo_list if a.get("completed") is True]

    # Print employee's name and number of tasks completed
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todo_list)
    ))

    for complete in completed:
        print("\t {}".format(complete))

    # Export data to JSON file
    tasks = []
    for task in todo_list:
        task_dict = {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": employee.get("username")
        }
        tasks.append(task_dict)

    json_data = {str(employee_id): tasks}

    json_filename = "{}.json".format(employee_id)
    with open(json_filename, 'w') as json_file:
        json.dump(json_data, json_file)
