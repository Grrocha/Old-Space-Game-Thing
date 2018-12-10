import Spaceships.Spaceship as ss
import ShipModules.Modules as sm

class Player(object):
    def __init__(self, HP, PID, Username, Inventory, IsBoarded, Position, Credits):
        self.HP = HP
        self.PID = PID
        self.Username = Username
        self.Inventory = Inventory
        self.IsBoarded = IsBoarded
        self.Position = Position
        self.Credits = Credits