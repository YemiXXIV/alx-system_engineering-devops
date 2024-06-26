#!/usr/bin/python3
"""
This script is to return the to-do list information of a given
employee id

This script takes a command-line argument and fetches the
corresponding data and to-do list from the provided API, then
prints the tasks completed by the employee.
"""


import requests
import sys


if __name__ == "__main__":
    url_api = "https://jsonplaceholder.typicode.com/"

    # To get employee information using the employee ID
    employee_id = sys.argv[1]
    employee = requests.get(url_api + "users/{}".format(employee_id)).json()

    # To get to-do list for the employee using the employee ID
    values = {"userId": employee_id}
    todo_list = requests.get(url_api + "todos", values).json()

    completed = [
        a.get("title") for a in todo_list if a.get("completed") is True]

    # Print employee's name and number of tasks completed
    print("Employee {} is done with tasks({}/{}):".format(
        employee.get("name"), len(completed), len(todo_list)))

    [print("\t {}".format(complete)) for complete in completed]
