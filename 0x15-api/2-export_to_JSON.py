#!/usr/bin/python3
"""gets infor from REST API"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1])
    todo_url = ('https://jsonplaceholder.typicode.com/users/'
                '{}/todos'.format(argv[1]))

    user_info = requests.get(user_url).json()
    tasks = requests.get(todo_url).json()

    json_string = json.dumps({argv[1]: [{'task': task.get('title'),
                                         'completed': task.get('completed'),
                                         'username': user_info.get('username')}
                                        for task in tasks]})

    filename = '{}.json'.format(argv[1])
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json_string)
