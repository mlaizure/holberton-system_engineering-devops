#!/usr/bin/python3
"""gets infor from REST API"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    user_url = 'https://jsonplaceholder.typicode.com/users'
    users = requests.get(user_url).json()

    all_dict = {}
    for i, user in enumerate(users):
        todo_url = ('https://jsonplaceholder.typicode.com/users/'
                    '{}/todos'.format(i))
        tasks = requests.get(todo_url).json()

        user_list = [{'task': task.get('title'),
                      'completed': task.get('completed'),
                      'username': user.get('username')}
                     for task in tasks]
        all_dict[user.get('id')] = user_list

    json_string = json.dumps(all_dict)
    filename = 'todo_all_employees.json'
    with open(filename, mode='w', encoding='utf-8') as f:
        f.write(json_string)
