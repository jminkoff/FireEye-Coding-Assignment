#code for server client written in python compatible with python 3

import socket
import sys
from os.path import exists
from pathlib import Path
import os.path

HOST = "127.0.0.1"
PORT = 65532

#socket object at client side
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#connecting to the server
sock.connect((HOST,PORT))

while True:

    #recieve prompt sent from server side
    print(sock.recv(4096).decode())#working

    #take identifier from the user
    id = input("Identifier: ")

    sock.send(id.encode())
    print("You will be prompted for a password, if your password is incorrect the socket will close. If your password is correct the data you are sending to the server will be written to a file titled output")

    #print the next prompt
    #print(sock.recv(4096).decode())

    #enter password
    password = input("Password: ")

    #send password back to server side to verify
    sock.send(password.encode())

    #print if access is Denied
    #print(sock.recv(4096).decode())

    #send data to server to be written to file
    msg = input("Please enter a message to send to the server: ")

    sock.send(msg.encode())
    #write to file on server side







sock.close()
