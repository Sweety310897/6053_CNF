import socket
import random
import threading
def main():
    host = '10.10.9.61'
    port = 1532
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print("server has started")
    while True :
        c, addr = s.accept()
        threading.Thread(target = checknumber, args = (c)).start()    
        print("Connection is established from:"+ str(addr))
        str1 = "enter roll number"
        c.send(str1.encode())
        temp100 = c.recv(1024).decode()
        threading.Thread(target = checknumber, args = (c)).start()
    s.close()
def checknumber(c):
    temp = load_file("data.csv")
    while True:
        data = c.recv(1024).decode()
        print("Guess :" + str(data) + "Client Addr: "+str(addr))
        for each in temp:
            if int(data) in temp:
                send = "Correct, rollnum " + str(count)
                c.send(send.encode())
                break
    c.close()
def load_file(filename):
    dic = {}
    with open(filename, 'r') as filename:
        for line in filename:
            temp1 = line.split(",")
            dic[temp1[0]] = temp1[1] + temp1[2]
    return dic
if __name__ == "__main__":
    main()
