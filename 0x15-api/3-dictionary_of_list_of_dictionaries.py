#!/usr/bin/python3
"""
This script fetches the to-do list information of all employees and exports the data to a JSON file.

The script retrieves data from the provided API and exports all tasks for each employee to a JSON file in the specified format.
"""

import json
import requests


if __name__ == "__main__":
    url_api = "https://jsonplaceholder.typicode.com/"

    # To get information for all users
    users = requests.get(url_api + "users").json()

    # Dictionary to hold all users' tasks
    all_tasks = {}

    # Iterate through each user to get their tasks
    for user in users:
        user_id = user.get("id")
        username = user.get("username")

        # To get to-do list for the current user
        values = {"userId": user_id}
        todo_list = requests.get(url_api + "todos", params=values).json()

        # List to hold task details for the current user
        tasks = []
        for task in todo_list:
            task_dict = {
                "username": username,
                "task": task.get("title"),
                "completed": task.get("completed")
            }
            tasks.append(task_dict)

        # Add the user's tasks to the all_tasks dictionary
        all_tasks[str(user_id)] = tasks

    # Export data to JSON file
    json_filename = "todo_all_employees.json"
    with open(json_filename, 'w') as json_file:
        json.dump(all_tasks, json_file)
