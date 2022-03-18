import socket

serverip = 'localhost'
#serverip = '192.168.1.37'
port = 7000

while True:
    data = input('Enter Message: ')
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.connect((serverip, port))
    server.send(data.encode('utf-8'))
    
    data_server = server.recv(1024).decode('utf-8')
    print('Data from server: ', data_server)
    server.close()