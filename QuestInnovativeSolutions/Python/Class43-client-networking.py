import socket

c=socket.socket()
print('socket created')

c.connect(('localhost',9999))

name=input('Enter the name')
c.send(name.encode())
print(c.recv(100).decode())     #100-just a argument --length of a message that may be any number
