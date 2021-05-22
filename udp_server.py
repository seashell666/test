from socket import *

sockfd=socket(AF_INET,SOCK_DGRAM)

server_addr=('127.0.0.1',20007)
sockfd.bind(server_addr)

while True:
    data,addr=sockfd.recvfrom(1024)
    print('receive:',data.decode())
    sockfd.send(b'Thanks',server_addr)

sockfd.close()