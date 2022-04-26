#server code written in python
import socket
import sys
from os.path import exists
from pathlib import Path
import os.path

#create socket objects
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#print socket made

HOST = "127.0.0.1" #loopback address
PORT = 65532

#binding socket with server and port number (needs to be done on server side)
sock.bind((HOST,PORT))

#we only want 1 connection
sock.listen(1)

while True:
    #get address and client object after client accepts the connection
    cl, add = sock.accept()

    #sending a message to client as a prompt
    prompt1 = "Please enter an identifier: "

    cl.send(prompt1.encode())

    #print(cl.recv(4096).decode())

    if cl.recv(4096):
        #prompt2 = "Welcome "+ cl.recv(4096).decode() + "!"+" Please enter the password: "
        #cl.send(prompt2.encode())

            #once prompted get the password from the user in this case the password is just "password" (ideally this would be a lot more intricate for practical application)
        if cl.recv(4096).decode()=="password":
            #access = "Access Granted"
            #cl.send(access.encode())
            if os.path.exists("output.txt"): os.remove("output.txt") #check if file exists on the server if so remove it
            file = open("output.txt",'w')

            msg = cl.recv(4096).decode()

            file.write(msg)
            #now I will read out the message printed to output.txt to the screen
            print("Message written to the file: ")
            #ensure message gets written
            file = open("output.txt","r")
            print(file.read())

            file.close()


        else:
            access = "Access Denied"
            #cl.send(access.encode())
            sock.close()







sock.close()
