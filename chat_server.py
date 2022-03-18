import socket
import datetime
import threading
import config


PORT = config.PORT
BUFSIZE = config.BUFSIZE
SERVERIP = config.SERVERIP

clist = [] # client list

def client_handler(client, addr):
    while True:
        try: #ลองทำอันนี้ได้ไหม
            data = client.recv(BUFSIZE)
        except: # ถ้าไม่ได้มาอันนี้แทน
            clist.remove(client)
            break
        if (not data) or (data.decode('utf-8') == 'q'):
            clist.remove(client)
            print('OUT: ', client)
            break
        
        msg = str(addr) + '>>> '+ data.decode('utf-8')
        print('USER: ')
        print('-------------------')
        for c in clist:
            c.sendall(msg.encode('utf-8'))
            
    client.close()
    
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVERIP, PORT))
server.listen(5)

while True:
    client, addr = server.accept()
    clist.append(client)
    print('ALL CLIENT: ', clist)
    
    task = threading.Thread(target= client_handler, args=(client, addr))
    task.start()
            