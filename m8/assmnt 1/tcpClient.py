import socket
def main():
	host = '10.10.9.61'
	port = 5111
	s = socket.socket()
	s.connect((host, port))
	message = input("input is:")
	while message != "q":
		s.send(message.encode())
		data = s.recv(1024)
		print("message is recieved here:" + str(data.decode()))
		message = input("Input is:")
	s.close()
if __name__ == '__main__':
	main()