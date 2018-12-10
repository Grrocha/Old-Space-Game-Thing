class Engine(object):
    def __init__(self,Force,Vector,FuelConsumption,Firing, Mass, Name,PID, HP):
        self.Force = Force
        self.Vector = Vector
        self.FuelConsumption = FuelConsumption
        self.Mass = Mass
        self.Name = Name
        self.PID = PID
        self.HP = HP
class FuelTank(object):
    def __init__(self,Cap , Mass, Name,PID, HP):
        self.Cap = Cap
        self.Mass = Mass
        self.Name = Name
        self.PID = PID
        self.HP = HP
class Utilitary(object):
    def __init__(self, FiringFunction, Mass, Name, PowerCon, Parent,PID, HP):
        self.FiringFunction = FiringFunction
        self.Mass = Mass
        self.Name = Name
        self.PowerCon = PowerCon
        self.Parent = Parent
        self.PID = PID
        self.HP = HP
class FuelGenerator(object):
    def __init__(self,Mass, PowerGen, FuelConsumption, OnOff,PID, HP):
        self.PowerGen = PowerGen
        self.FuelConsumption = FuelConsumption
        self.OnOff = OnOff
        self.PID = PID
        self.HP = HP
        self.Mass = Mass
class CargoBay(object):
    def __init__(self,Mass, PID, HP, Volume):
        self.PID = PID
        self.HP = HP
        self.Volume = Volume
        self.Mass = Mass