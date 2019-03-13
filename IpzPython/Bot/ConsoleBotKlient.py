import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 80))
serversocket.listen(5)
print('Server is waiting for connections.')
while True:
    conn, addr = serversocket.accept()
    data = conn.recv(1024)

    print('Connection:', addr)
    print('------------------------------')
    print("Request Data from Browser")
    print('------------------------------')
    print(data)

    conn.send(data)
    conn.close()
    time.sleep(0.1)  # delay
