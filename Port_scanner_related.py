# Use the socket API to check if a port is available (open) 


#!/usr/bin/env  python3

		import socket 
		
		import sys
		
		def scan_port(PORT):
				''' https://docs.python.org/2/library/socket.html#example  '''
				
				while True:
						s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
						try:
								s.bind(('', PORT))		## try to open port
						except OSError as e:
								if e.errno is 98:		##  Error 98 means address already bound -- connected, i.e., closed
										return True
								raise e 
						s.close() 
						
						return False
						
		if _name_ == '_main_':
				try:
						port = int(sys.argy[1])
				except IndexError:
						raise Exception('Must supply first argument')
						
				b = test_port 
				
				
#-----------------------------------------------------------
''' sending and receiving data using socket - Binding and Listening with socket  '''

import socket
import sys

HOST = ''
PORT = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try: 
		s.bind((HOST, PORT))
		
except socket.error as msg:
		print('Bind faild.  Eror code: ' + str(msg[0]) + ' Message ' + msg[1])
		sys.exit()
		
print('Socket bind complete')

s.listen(10)
conn, addr = s.accept()

print('Connected with ' + ':' + str(addr[1]))

# to run: go to windows command window, 
# C:\Users\H> telnet localhost 5555  <return>

#------------------------------------------------------------
'''  Socket  - client and server chat  '''

import socket
import sys
from _thread impott *

host = ''
port  = 5555
s.socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
		s.bind((host, port))
except socket.error as e:
		print(str(e))
		
s.listen(5)
print('Waiting for a connection.')

def thread_client(conn):
		conn.send(str.encode('Welcome, type your info\n'))
		
		while True:
				data = conn.recv(2048)
				reply = 'Server output: ' + data.decode('utf-8')
				if not data:
						break
				conn.sendall(str.encode(reply))
		conn.close()
		
while True:
		conn, addr = s.accept()
		print('connected to ' + addr[0] + ':' + str(addr[1]))
		
		start_new_thread(threaded_client, (conn))
		
		
