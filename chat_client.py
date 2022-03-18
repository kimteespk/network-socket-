import socket, threading, config, sys



PORT = config.PORT
BUFSIZE = config.BUFSIZE
SERVERIP = config.SERVERIP

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

def server_handler(client):
    while True:
        try:
            data = client.recv(BUFSIZE)
        except:
            print('ERROR!')
            break
        if (not data) or (data.decode('utf-8') == 'q'):
            print('OUT!')
            break
        
        print('USER: ',data.decode('utf-8'))
        
    client.close()
        


try:
    client.connect((SERVERIP, PORT))
except:
    print('ERROR!')
    sys.exit()
    
    
task = threading.Thread(target= server_handler, args=(client,))
task.start()


while True:
    msg = input('Message: ')
    client.sendall(msg.encode('utf-8'))
    if msg == 'q':
        break
    
client.close()