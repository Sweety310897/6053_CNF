import socket
import threading
import os, signal
s = socket.socket()
def main():
	host = '10.10.9.61'
	port = 1532
	s.connect((host, port))
	welcomeMsg = s.recv(1024).decode()
	print(welcomeMsg)
	s.send(input().encode())
	threading.Thread(target = client, args = ()).start()
	while True:
		try:
			msg = s.recv(1024).decode()
			print(msg)
			if msg == "ATTENDANCE-SUCCESS":
				os.kill(os.getpid(), signal.CTRL_BREAK_EVENT)
			if not msg:
				continue
		except:
			print("Oops!, Host server Closed by admin. you cannot send")
			break
	s.close()
def client():
	while True:
		msg = input("helo")
		if not msg:
			continue
		s.send(msg.encode())
	s.close()
if __name__ == '__main__':
	main()