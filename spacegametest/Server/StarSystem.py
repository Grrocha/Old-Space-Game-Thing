import Player as pl
import Spaceship as ss
import numpy as np

class System(object):
    def __init__(self, Name, MotherBody, PlayersInSystem, ObjectsInSystem, Active, Id, GalPosition):
        self.Name = Name
        self.MotherBody = MotherBody
        self.PlayersInSystem = PlayersInSystem
        self.ObjectsInSystem = ObjectsInSystem
        self.Active = Active
        self.Id = Id
        self.GalPosition = GalPosition #GalPosition will be in LY
        
    def update(self):
        if len(self.PlayersInSystem) > 0:
            self.Active = True
        else:
            self.Active = False
            return
        if self.Active == True:
            for i in self.PlayersInSystem:
                for x in self.ObjectsInSystem:
                    self.Gravitate(i, x)
            for i in self.ObjectsInSystem:
                for x in self.ObjectsInSystem:
                    self.Gravitate(i, x)
                    
    def Gravitate(self, Body1, Body2, Time):
        G = (6.67408 * (10^-11))
        Distance = np.sqrt((Body1.position[0] - Body2.position[0])^2 + (Body1.position[1] - Body2.position[1])^2 + (Body1.position[2] - Body2.position[2]^2))
        CosXV = (Body1.position[0] - Body2.position[0])/Distance
        CosYV = (Body1.position[1] - Body2.position[1])/Distance
        CosZV = (Body1.position[2] - Body2.position[2])/Distance
        
        Gravity = ((G*Body1.mass*1000)*(Body2.mass*1000))/(Distance^2)
        #ACTION...
        Body1.vel[0] += (Gravity/(Body1.mass*1000)*CosXV)*Time
        Body1.vel[1] += (Gravity/(Body1.mass*1000)*CosYV)*Time
        Body1.vel[2] += (Gravity/(Body1.mass*1000)*CosZV)*Time
        #...AND REACTION
        Body2.vel[0] = Body2.vel[0] - (Gravity/(Body2.mass*1000)*CosXV)*Time
        Body2.vel[1] = Body2.vel[1] - (Gravity/(Body2.mass*1000)*CosYV)*Time
        Body2.vel[2] = Body2.vel[2] - (Gravity/(Body2.mass*1000)*CosZV)*Time
        
class Body(object):
    def __init__(self, Name, Mass, Class, Composition, Id, Position, Vel, Rotation, TidalLock, Model, SID):
        self.Name = Name
        self.Mass = Mass
        self.Class = Class
        self.Composition = Composition
        self.Id = Id
        self.Position = Position
        self.Vel = Vel
        self.Rotation = Rotation
        self.TidalLock = TidalLock
        self.Model = Model
        self.SID = SID