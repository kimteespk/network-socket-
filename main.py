import socket
import random

word_list = ['chayote fruit', 'kundong', 'dekopon', 'rose apple', 'mamey sapote', 'ackee', 'agave plant', 'bilimbi', "dead man's fingers", 'korlan', 'charichuelo fruit', 'kahikatea', 'babaco', 'bilimbi', 'calamansi', 'clementines', 'nere', 'loquat', 'fibrous satinash', 'batuan fruit']


a = random.randint(00000, 99999)
stra = str(a)

serverip = '104.248.39.146'
server = socket.socket()
server.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
server.connect(('104.248.39.146',72017))#,port))
server.connect(('104.248.39.146',65535))#,port))

for i in range(100,1000):
    #if i < 10000:
        
    port = int(str(i) + '17')
    print(port)
    server.connect(('104.248.39.146',port))



### ** find port 
# * then connect to 
### ** use for/while loop to put word_list in any possibilities

