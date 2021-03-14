import socket
import threading


nickname = input("Choose your nickname: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 2233))


def receive():
    while True:
        try:
            message = client.recv(1024).decode('utf-32')
            if message == 'NICK':
                client.send(nickname.encode('utf-32'))
            else:
                print(message)
        except:
            print("An error occured!")
            client.close()
            break



def write():
    while True:
        message = '{}: {}'.format(nickname, input(''))
        client.send(message.encode('utf-32'))


receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()