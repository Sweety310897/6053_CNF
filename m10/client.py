import socket
import threading
import os, signal
s = socket.socket()
def main():
	host = '10.10.9.61'
	port = 5645
	s.connect((host, port))
	welcomeMsg = s.recv(1024).decode()
	print(welcomeMsg)
	s.send(input().encode())
	threading.Thread(target = sender, args = ()).start()
	while True:
		msg = s.recv(1024).decode()
		print(msg)
		if not msg:
			continue
	s.close()
def sender():
	while True:
		msg = input("give input")
		if not msg:
			continue
		s.send(msg.encode())
	s.close()
if __name__ == '__main__':
	main()