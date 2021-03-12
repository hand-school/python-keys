import socket
import threading


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('94.250.252.115', 5050))
client = []  # Массив где храним адреса клиентов
print('Start Server')
while 1:
    data, addres = sock.recvfrom(1024)
    print(addres[0], addres[1])
    if addres not in client:
        client.append(addres)  # Если такого клиента нету , то добавить
    for clients in client:
        if clients == addres:
            continue  # Не отправлять данные клиенту, который их прислал
        sock.sendto(data, clients)




def read_sok():
    while 1 :
        data = sor.recv(1024)
        print(data.decode('utf-8'))

 server = '192.168.0.1', 5050  # Данные сервера
 alias = input() # Вводим наш псевдоним
 sor = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
 sor.bind(('', 0)) # Задаем сокет как клиент
 sor.sendto((alias+' Connect to server').encode('utf-8'), server)# Уведомляем сервер о подключении
 potok = threading.Thread(target= read_sok)
 potok.start()
 while 1 :
     mensahe = input()
     sor.sendto(('['+alias+']'+mensahe).encode('utf-8'), server)


key = 567  # Ключ шифрования

crypt = ''
for i in  message  :
    crypt += chr(ord(i)^key)
 message  = crypt