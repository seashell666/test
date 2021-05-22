from socket import *
s=socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(('192.168.207.130',20007))
s.listen(3)
c,addr=s.accept()

print(c.getpeername())
c.recv(1024)
