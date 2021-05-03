#!/usr/bin/python3
"""gets infor from REST API"""
if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = ('https://jsonplaceholder.typicode.com/users/'
                '{}/todos'.format(argv[1]))

    user_info = requests.get(user_url).json()
    tasks = requests.get(todo_url).json()

    filename = '{}.csv'.format(argv[1])
    with open(filename, mode='w', encoding='utf-8') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in tasks:
            writer.writerow([argv[1], user_info.get('username'),
                             task.get('completed'), task.get('title')])
