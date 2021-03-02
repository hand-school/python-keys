import requests

# r = requests.get('http://localhost:5000/todo/api/v1.0/tasks')
# print(r.status_code)
# print(r.headers)
# print(r.text)

# r = requests.get('http://localhost:5000/todo/api/v1.0/tasks/2')
# print(r.status_code)
# print(r.headers)
# print(r.text)

payload = {
    'title': 'Test 2 POST',
    'description': 'Why am i doing this?',
    'done': False, }


#r = requests.post('http://localhost:5000/todo/api/v1.0/tasks', data=payload)

# r = requests.get('http://localhost:5000/todo/api/v1.0/tasks')
# print(r.text)

payload_2 = {
    'title': 'NOT test 2 POST',
    'description': 'Rewrite post 2',
    'done': False, }

r = requests.put('http://localhost:5000/todo/api/v1.0/tasks/1', data=payload_2)


r = requests.get('http://localhost:5000/todo/api/v1.0/tasks')

print(r.text)
