import requests

# r = requests.get('http://localhost:5000/todo/api/v1.0/tasks')
# print(r.status_code)
# print(r.headers)
# print(r.text)

r = requests.get('http://localhost:5000/todo/api/v1.0/tasks/2')
print(r.status_code)
print(r.headers)
print(r.text)

