#!/usr/bin/python
import socket
import random

status = 0
MyPort = 1234
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mySocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
mySocket.bind(('localhost', MyPort))

mySocket.listen(5)

while True:
	print '	Waiting for connections'
	(recvSocket, address) = mySocket.accept()
	print '	HTTP request recived:'
	request = recvSocket.recv(1024)
	print request


	slots = request.split(' ')
	try:
		num = int(slots[1][1:])
	except ValueError:
		msg = "La URL debe entregar un numero al final. Ejemplo: localhost:1234/56"
		recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + "<html><body>" + msg + "</body></html>" + "\r\n")
		status = 0

	if status == 0:
		sum1 = num
		msg = "El primer numero es " + str(sum1) + ". Introduce el segundo numero"
		status = 1
	else:
		sum2 = num
		res = str(sum1+sum2)
		msg = "Resultado de la suma: " + str(sum1) + " + " + str(sum2) + " = " + res
		status = 0


	recvSocket.send("HTTP/1.1 200 OK\r\n\r\n" + "<html><body>" + msg + "</body></html>" + "\r\n")
