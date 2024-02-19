from re import T
import socket

s=socket.socket()
print("Socket created")
#0-9999
s.bind(('localhost',9999))

s.listen()      #enable server to accept connection
print('Waiting for connection')

while True:
    c,address=s.accept()        #accept the connection from the client
    name=c.recv(100).decode()
    print('connected with',address,name) 
    c.send('Connected Succesfully'.encode())
    