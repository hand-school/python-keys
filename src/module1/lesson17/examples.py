import requests


r = requests.get('http://localhost:5000/todo/api/v1.0/tasks')

print(r.status_code)
print(r.headers)
print(r.text)
print("------------------------------------------")

r = requests.post('http://localhost:5000/todo/api/v1.0/tasks',
                  data={"title":"Neponiatnaya xuyta","description":"polnaya xuynia","done":True})
print(r.status_code)
print(r.text)
print("------------------------------------------")
r = requests.put('http://localhost:5000/todo/api/v1.0/tasks/1',data={"title":"Hi, my Dick","description":"Flax for Py - govno","done":True})
print(r.status_code)
print(r.headers)
print(r.text)
print("------------------------------------------")
r = requests.get('http://localhost:5000/todo/api/v1.0/tasks/3')
print(r.status_code)
print(r.headers)
print(r.text)
print("------------------------------------------")
r = requests.delete('http://localhost:5000/todo/api/v1.0/tasks/3')
print("------------------------------------------")
r = requests.get('http://localhost:5000/todo/api/v1.0/tasks/3')
print(r.status_code)
print(r.text)

