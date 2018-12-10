class Engine(object):
    def __init__(self,Force,Vector,FuelConsumption,Firing, Mass, Name,PID, HP, Offset):
        self.Force = Force
        self.Vector = Vector
        self.FuelConsumption = FuelConsumption
        self.Mass = Mass
        self.Name = Name
        self.PID = PID
        self.HP = HP
        self.Offset = Offset
class FuelTank(object):
    def __init__(self,Cap , Mass, Name,PID, HP, Offset):
        self.Cap = Cap
        self.Mass = Mass
        self.Name = Name
        self.PID = PID
        self.HP = HP
class Utilitary(object):
    def __init__(self, FiringFunction, Mass, Name, PowerCon, Parent,PID, HP, Offset):
        self.FiringFunction = FiringFunction
        self.Mass = Mass
        self.Name = Name
        self.PowerCon = PowerCon
        self.Parent = Parent
        self.PID = PID
        self.HP = HP
        self.Offset = Offset
class FuelGenerator(object):
    def __init__(self,Mass, PowerGen, FuelConsumption, OnOff,PID, HP, Offset):
        self.PowerGen = PowerGen
        self.FuelConsumption = FuelConsumption
        self.OnOff = OnOff
        self.PID = PID
        self.HP = HP
        self.Mass = Mass
        self.Offset = Offset
class CargoBay(object):
    def __init__(self,Mass, PID, HP, Volume, Inventory, Offset):
        self.PID = PID
        self.HP = HP
        self.Volume = Volume
        self.Mass = Mass
        self.Offset = Offset