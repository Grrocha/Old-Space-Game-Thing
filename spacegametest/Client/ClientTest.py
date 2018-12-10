import socket
import json
Username = "1"
Password = "x"
Connected = False
clientsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
clientsock.settimeout(5)
port = 25000
server = 'brspgurocha', int(port)
Salt = 0
ClientVersion = "1"

def connect(Username, Password, socket, port, server):
    global Connected
    global Salt
    msg = {"Protocol": "cr", "Data": [Username, Password, ClientVersion]}
    data = json.dumps(msg)
    print(data)
    clientsock.sendto(data.encode(), server)
    Response = json.loads(clientsock.recv(2048).decode())
    if Response["Protocol"] == "ca":
        print(Response["Data"][0])
        Connected = True
        Salt = Response["Data"][1]
        print(Salt)
    if Response["Protocol"] == "cd":
        Connected = False
        RejectMessage = Response["Data"][0]
        print(RejectMessage)

Username = input("Please Insert Username>>>")
Password = input("Please Insert Password>>>")
connect(Username, Password, clientsock, port, server)
while Connected == True:
    try:
        Received, address = clientsock.recvfrom(2048)
        print(json.loads(Received.decode()))
    except Exception as ex:
        pass