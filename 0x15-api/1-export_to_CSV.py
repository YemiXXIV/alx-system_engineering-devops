#!/usr/bin/python3
"""
This script is to return the to-do list information of a given
employee id and export the data to a CSV file.

This script takes a command-line argument and fetches the
corresponding data and to-do list from the provided API, then
prints the tasks completed by the employee and exports all tasks
to a CSV file.
"""

import csv
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

    # Export data to CSV file
    csv_filename = "{}.csv".format(employee_id)
    with open(csv_filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for task in todo_list:
            writer.writerow([employee_id, employee.get("username"),
                             task.get("completed"), task.get("title")])
