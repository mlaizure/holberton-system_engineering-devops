#!/usr/bin/python3
"""gets infor from REST API"""
if __name__ == "__main__":
    import requests
    from sys import argv

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = ('https://jsonplaceholder.typicode.com/users/'
                '{}/todos'.format(argv[1]))

    user_info = requests.get(user_url).json()
    param = {'completed': 'true'}
    completed_tasks = requests.get(todo_url, params=param).json()
    tasks = requests.get(todo_url).json()

    print('Employee {} is done with tasks({}/{})'
          ':'.format(user_info.get('name'), len(completed_tasks), len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task.get('title')))
