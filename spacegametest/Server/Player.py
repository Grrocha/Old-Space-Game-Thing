class Player(object):
    def __init__(self, PID, Slot, Username, Party, Lastconn, Salt):
        self.PID = PID
        self.Slot = Slot
        self.Username = Username
        #self.Inventory = Inventory
        #self.IsBoarded = IsBoarded
        #self.Position = Position
        #self.Rotation = Rotation
        #self.State = State
        self.Party = Party
        self.Lastconn = Lastconn
        self.Salt = Salt