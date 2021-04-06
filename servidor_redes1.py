import socket
import sys

HOST = ''  # Nombre o direccion de la maquina. Puede estar vacio en el servidor
PORT = 8888  # Puerto de escucha del servidor. PORT >= 5000
BUFFER = 1000 # Tamano del buffer de recepcion

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print 'Socket creado...'

# Enlaza el socket con la direccion y puerto local
try:
	s.bind((HOST, PORT))

# Captura excepciones. Si existe, un error sale del programa
except socket.error as msg:
	print 'Fallo en BIND. Cod. Error: ' + str(msg[0]) + ' Mensaje ' + msg[1]
	sys.exit()
print 'Socket Enlazado...'

# Comienza la escucha en el socket
s.listen(10)
print 'Socket escuchando...'

while 1:
	try:

		# Espera a que lleguen clientes.
		cliente, addr = s.accept()
		print 'Conectado con ' + addr[0] + ':' + str(addr[1])
		
		while 1:
			# Recepcion de datos
			datos = cliente.recv (BUFFER)
			if datos:
				cliente.send (datos)
				print 'Recibido: ' + datos
			 # Se dejara de trabajar con el cliente si se recibe EXIT
				if datos[0:4] == 'EXIT':
					cliente.close() 
					break
	except KeyboardInterrupt:
		print '\nCerrando socket y apagando servidor...'
		s.close()
		break
		
s.close()
