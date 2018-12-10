import Modules as sm
class spaceship(object):
    #we'll never know why i've placed "plcontrollable" in the fucking server script
    def __init__(self,hullclass,vel,rotvel,modules,mass,fuel,assist,position,rot,name,ssid, hasengine, totalthrust, maxfuel, FiringEngines, MovVector, TotalConsumption, totalmass, power, totalpower, PowerGen,PID, CargoVol, Cargo, Controlling, Owner, Effects, Temperature, Crew, Fleet, State):
        self.hullclass = hullclass
        self.vel = vel
        self.rotvel = rotvel
        self.rot = rot
        self.modules = modules
        self.mass = mass
        self.fuel = fuel
        self.assist = assist
        self.position = position
        self.name = name
        self.ssid = ssid
        self.hasengine = hasengine
        self.totalthrust = totalthrust
        self.maxfuel = maxfuel
        self.FiringEngines = FiringEngines
        self.MovVector = MovVector
        self.TotalConsumption = TotalConsumption
        self.totalmass = totalmass
        self.PowerGen = PowerGen
        self.power = power
        self.totalpower = totalpower
        self.PID = PID
        self.CargoVol = CargoVol
        self.Cargo = Cargo
        self.Controlling = Controlling
        self.Owner = Owner
        self.Effects = Effects
        self.Temperature = Temperature
        self.Crew = Crew
        self.Fleet = Fleet
    def updatemodules(self):
        self.hasengine = False
        self.totalthrust = 0.0
        self.maxfuel = 0.0
        self.mass = 0.0
        self.totalpower = 0.0
        self.PowerGen = 0.0
        self.TotalConsumption = 0.0
        self.CargoVol = 0.0
        for i in self.modules:
            if self.modules[i].__class__.__name__ == "Engine":
                self.hasengine = True
                self.totalthrust += self.modules[i].Force
                self.mass += self.modules[i].Mass
                self.modules[i].PID = self.PID
                self.TotalConsumption += self.modules[i].FuelConsumption
            elif self.modules[i].__class__.__name__ == "FuelTank":
                self.maxfuel += self.modules[i].Cap
                self.mass += self.modules[i].Mass
                self.modules[i].PID = self.PID
            elif self.modules[i].__class__.__name__ == "Utilitary":
                self.mass += self.modules[i].Mass
                self.modules[i].PID = self.PID
            elif self.modules[i].__class__.__name__ == "FuelGenerator":
                self.PowerGen += self.modules[i].PowerGen
                self.TotalConsumption += self.modules[i].FuelConsumption
                self.modules[i].PID = self.PID
                self.mass += self.modules[i].Mass
            elif self.modules[i].__class__.__name__ == "CargoBay":
                self.modules[i].PID = self.PID
                self.mass += self.modules[i].Mass
                self.CargoVol += self.modules[i].Volume
    def update(self):
        CargoMass = 0
        for item in self.Cargo:
            CargoMass += item.Vol*item.Density
        self.totalmass = self.mass + self.fuel/1000 + CargoMass/1000
        if self.fuel > 0:
            if self.assist == True:
                if self.hasengine == True and self.FiringEngines == False:
                    for v in self.vel:
                        if v < 0:
                            v += self.totalthrust/self.mass
                        elif v > 0:
                            v -= self.totalthrust/self.mass
                    self.fuel -= self.TotalConsumption
                elif self.FiringEngines == True:
                    self.vel[0] += self.MovVector[0]*(self.totalthrust/self.totalmass)
                    self.vel[1] += self.MovVector[1]*(self.totalthrust/self.totalmass)
                    self.vel[2] += self.MovVector[2]*(self.totalthrust/self.totalmass)
                    self.fuel -= self.TotalConsumption
            elif self.assist == False:
                if "Engine" in self.modules.keys():
                    if self.FiringEngines == True:
                        self.vel[0] += self.MovVector[0]*(self.totalthrust/self.totalmass)
                        self.vel[1] += self.MovVector[1]*(self.totalthrust/self.totalmass)
                        self.vel[2] += self.MovVector[2]*(self.totalthrust/self.totalmass)
                        self.fuel -= self.TotalConsumption
        for i in self.modules:
            print(self.modules[i].__class__.__name__)               
        self.position[0] += self.vel[0]           
        self.position[1] += self.vel[1]
        self.position[2] += self.vel[2]
        
#Starkick = spaceship("Frigate",[0,0,0],[0,0,0],{},0.0,10.0,True,[0,0,0],[0,0,0],"Starkick","SK-11",True,False,0.0,0.0, False, [0,0,0],0.0,0.0,0.0,0.0)
#Starkick.updatemodules()
#Starkick.update()
#print("Fuel: " + str(Starkick.fuel) +"/" + str(Starkick.maxfuel)+"Kg")
#print("Thrust: " + str(Starkick.totalthrust) + "Kn")
#print("Mass: " + str(Starkick.totalmass) + "T")