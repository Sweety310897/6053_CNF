import socket
def main():
	host = '10.10.9.61'
	port = 1518
	s = socket.socket()
	s.connect((host, port))
	print("Connecting to Server\n")
	print("Connected!\n")
	str1 = s.recv(1024).decode()
	str2 = s.recv(1024).decode()
	print(str(str1))
	print(str(str2) + "\n")
	message = input("enter your guess: number")
	while message != 'q':
		s.send(message.encode())
		data = s.recv(1024).decode()
		print(str(data))
		message = input("enter your guess: number")
	s.close()
if __name__ == '__main__':
	main()