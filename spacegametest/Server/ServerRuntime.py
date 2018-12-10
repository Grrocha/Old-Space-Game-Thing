import socket
import time
import StarSystem as system
import Player as pl
import random
import json
import sqlalchemy

ServerVersion = "1"
PlayerSlots = 4
Port = 25000
serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind((socket.gethostname(), Port))
print("Server started at " + str(socket.gethostname()) + ":" + str(Port))
PlayersOnServer = {}
SystemList = {}
ConnectedUsers = []
clock = time.time()
serversocket.setblocking(0)
sqlengine = sqlalchemy.create_engine('mssql+pyodbc://sgtdb')
ServerRunning = False
InitialTime = 0

def InitiateServer():
    global ServerRunning
    global SystemList
    global InitialTime
    ServerStartTime = time.time()
    sqlconn = sqlengine.connect()
    Results = sqlconn.execute('select * from StarSystem_Info')
    for row in Results:
        SystemList[row['SID']] = system.System(str(row['SystemName']),"",{},{},row['Active'],row['SID'],[row['Galactic_PositionX'],row['Galactic_PositionY'],row['Galactic_PositionZ']])
        print("Initiating System " + str(row['SID']) + ": " + str(row['SystemName']))
    for i in SystemList:
        Results = sqlconn.execute('select * from StarSystem_Objects where SID = '+ str(i))
        for row in Results:
            SystemList[i].ObjectsInSystem[row['Id']] = system.Body(row['Name'],0,row['Class'],{},row['Id'],[row['Body_PosX'],row['Body_PosY'],row['Body_PosZ']],[row['Body_VelX'],row['Body_VelY'],row['Body_VelZ']],[row['Body_RotX'],row['Body_RotY'],row['Body_RotZ']],row['TidalLock'],row['Model'],row['SID'])
            print("Initiating Body " + str(row['Id']) + ": " + str(row['Name']) + " At System " + str(i) + ": " + SystemList[i].Name)
    InitialTime = time.time()
    StartupTime = InitialTime - ServerStartTime
    print("Server startup succeeded in " + str(StartupTime))
    ServerRunning = True
    sqlconn.close()
    
def UpdateServer(clock):
    global InitialTime
    global ConnectedUsers
    DeltaTime = time.time() - InitialTime
    clock2 = time.time()
    RefreshList = []
    while clock2 - clock < 0.016:
        clock2 = time.time()
    if clock2 - clock >= 0.016:
        for i in SystemList:
            SystemList[i].update(DeltaTime)
    for i in PlayersOnServer:
        RefreshList.append(PlayersOnServer[i].Username)
    ConnectedUsers = RefreshList
    clock = time.time()

def GenerateSalt(Player):        
    Player.Salt = random.randint(1,99999999)

def Connect(User, Pass):
    print("Connection Request From: " + User)
    try:
        sqlconn = sqlengine.connect()
        Results = sqlconn.execute('select * from Usersettings where Username = ' + User)
        row = Results.fetchone()
        sqlconn.close()
    except Exception as ex:
        print(ex)
        
    if str(User) == str(row['Username']) and str(Pass) == str(row['Password']):
        try:
            PlayersOnServer[address] = pl.Player(row['PID'],[],User,row['Party'], time.time(),0)
            MsgStr = 'Sucessfuly connected, welcome'
            print(PlayersOnServer)
            GenerateSalt(PlayersOnServer[address])
            #CA - Connection Accepted
            msg = {"Protocol": "ca", "Data": [MsgStr, PlayersOnServer[address].Salt]}
            data = json.dumps(msg)
            serversocket.sendto(data.encode('utf-8'), address)
            msg = {"Protocol": "msg", "Data": PlayersOnServer[address].Username + " has logged in"}
            data = json.dumps(msg)
            for i in PlayersOnServer.keys():
                serversocket.sendto(data.encode('utf-8'), i)
        except Exception as ex:
            #If user cannot connect, we pop him from the virtual connection slots
            print("User could not connect, error: " + str(ex))
            PlayersOnServer.pop(address)
            print(PlayersOnServer)
    else:
        #CD - Connection Denied
        MsgStr = 'Could not connect: Invalid Username or Password'
        msg = {"Protocol": "cd", "Data": [MsgStr]}
        data = json.dumps(msg)
        serversocket.sendto(data.encode('utf-8'),address)

def CheckMessage(Received):
    # CR - Connection Request
    if Received["Protocol"] == 'cr':
        Username = Received["Data"][0]
        Password = Received["Data"][1]
        #serversocket.settimeout(0.016)
        if Received["Data"][2] != ServerVersion:
            MsgStr = 'Could not connect: Outdated Client Version'
            msg = {"Protocol": "cd", "Data": [MsgStr]}
            data = json.dumps(msg)
            serversocket.sendto(data.encode('utf-8'),address)
        elif len(PlayersOnServer) < PlayerSlots:
            print("New connection request accepted")
            Connect(Username, Password)
        else:
            MsgStr = "Could not connect: Server is full"
            msg = {"Protocol": "cd", "Data": [MsgStr]}
            serversocket.sendto(msg.encode('utf-8'), address)
            print(MsgStr)
    elif Received["Protocol"] == "cmsg":
        #serversocket.settimeout(5)
        Message = Received["Data"][0]
        #serversocket.settimeout(0.016)
        Sender = PlayersOnServer[address].Username
        ChatMessage = str(Sender) + " says: " + Message.decode()
        for i in PlayersOnServer.keys():
            serversocket.sendto(ChatMessage.encode('utf-8'), i)
        
InitiateServer()
        
while ServerRunning == True:
    try:
        #(Received, address) = serversocket.accept()
        Received, address = serversocket.recvfrom(2048)
        ReceivedPacket = json.loads(Received.decode())
        print(ReceivedPacket)
        CheckMessage(ReceivedPacket)
        print("PACKET FROM " + str(address) + ": " + str(Received))
    except Exception as ex:
        pass
    UpdateServer(clock)