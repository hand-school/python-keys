import requests

# r = requests.get('http://localhost:5000/todo/api/v1.0/tasks')
# print(r.status_code)
# print(r.headers)
# print(r.text)

r = requests.get('http://localhost:5000/todo/api/v1.0/tasks/2')
print(r.status_code)
print(r.headers)
print(r.text)

r = requests.put('http://localhost:5000/todo/api/v1.0/tasks/2', data={'id': 1,
                                                                    'title': u'Buy groceries',
                                                                    'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
                                                                    'done': False})
print(r.status_code)
print(r.headers)
print(r.text)

# r = requests.post('http://localhost:5000/todo/api/v1.0/tasks', data={'id': 1,
#                                                                     'title': u'Buy groceries',
#                                                                     'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
#                                                                     'done': False})
# print(r.status_code)
# print(r.headers)
# print(r.text)

# r = requests.delete('http://localhost:5000/todo/api/v1.0/tasks/2')
# print(r.status_code)
# print(r.headers)
# print(r.text)
