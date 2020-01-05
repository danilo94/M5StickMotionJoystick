import socket
from KeyController import *
import struct
# bind all IP
HOST = '192.168.100.6'
# Listen on Port
PORT = 44444
#Size of receive buffer
BUFFER_SIZE = 1024
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Bind the socket to the host and port
s.bind((HOST, PORT))
controladorTeclado = KeyController()
while True:
    # Receive BUFFER_SIZE bytes data
    # data is a list with 2 elements
    # first is data
    #second is client address
    data = s.recvfrom(BUFFER_SIZE)
    if data:
        decoded= int(data[0].decode('utf-8'))
        print(decoded)
        left = False
        right = False
        a = False
        b = False
        if (decoded & 1) == 1:
            controladorTeclado.pressionar(0)
            left = True
        if (decoded & 2) == 2:
            controladorTeclado.pressionar(1)
            right = True
        if (decoded & 4) == 4:
            controladorTeclado.pressionar(2)
            a = True
        if (decoded & 8) == 8:
            b = True
        print(left,right,a,b)



s.close()


def decodeButton(value):
    left = False
    up = False
    a = False
    b = False
    if value & 1 == 1:
        left = True
    if value & 2 == 1:
        up = True
    if value & 4 == 1:
        a = True
    if value & 8 == 1:
        b = True

    return left,up,a,b
