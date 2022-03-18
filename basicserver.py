# basicserver.py


import socket

serverip = 'localhost'
#serverip = '192.168.1.37'
port = 7000

while True:
    server = socket.socket()
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    server.bind((serverip, port))
    server.listen(5)
    print('wating for client...')
    
    client, addr = server.accept()
    print('Connect from: ', str(addr))
    data = client.recv(1024).decode('utf-8')  # set จำนวนขนาด data ที่รับได้ 1024 byte 
    print('Message from client: ', data)
    client.send('We received your message!'.encode('utf-8'))
    client.close()
    
    
    

# เอาเอา โต้อิมพอ class ออก