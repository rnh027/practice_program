import socket

#first 3 line is important to create and access socket
#create object
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#made connection
mysock.connect(('data.pr4e.org', 80))
#access web data alternate way is using telnet
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
