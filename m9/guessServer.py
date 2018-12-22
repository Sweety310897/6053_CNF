import socket
import random
import threading
def main():
    host = '10.10.9.61'
    port = 1518
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("Server started")
    while True :
        c, addr = s.accept()
        print("Connection from: "+ str(addr))
        str1 = "Welcome to 'Guess my Nmber'!"
        str2 = "Try to guess a num between 1 to 100"
        c.send(str1.encode())
        c.send(str2.encode())
        threading.Thread(target = guessnumber, args = (c, addr)).start()
def guessnumber(c, addr):
    number = random.randint(1, 101)
    count = 0
    while True:
        data = c.recv(1024).decode()
        print("Guess :" + str(data) + "Client Address is: "+str(addr))
        if not data:
            break
        if int(data) == number:
            count += 1
            send = "Correct, number of guess : " + str(count)
            c.send(send.encode())
            break
        elif int(data) < number:
            count += 1
            send = "Your number is less than the guess"
            c.send(send.encode())
        elif int(data) > number:
            count += 1
            send = "Your number is greater than the guess"
            c.send(send.encode())
    c.close()
if __name__ == "__main__":
    main()
