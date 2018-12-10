import Player.Player as pl
import Spaceships.spaceship as ss
import numpy as np

class System(object):
    def __init__(self, Name, MotherBody, PlayersInSystem, ObjectsInSystem, Active, Id):
        self.Name = Name
        self.MotherBody = MotherBody
        self.PlayersInSystem = PlayersInSystem
        self.ObjectsInSystem = ObjectsInSystem
        self.Active = Active
        self.Id = Id
        
    def update(self):
        if self.PlayersInSystem.len() > 0:
            self.Active = True
        else:
            self.Active = False
        if self.Active == True:
            for i in self.PlayersInSystem:
                for x in self.ObjectsInSystem:
                    self.Gravitate(i, x)
            for i in self.ObjectsInSystem:
                for x in self.ObjectsInSystem:
                    self.Gravitate(i, x)
                    
    def Gravitate(self, Body1, Body2):
        Distance = np.sqrt((Body1.position[0] - Body2.position[0])^2 + (Body1.position[1] - Body2.position[1])^2 + (Body1.position[2] - Body2.position[2]^2))
        CosXV = Distance/(Body1.position[0] - Body2.position[0])
        CosYV = Distance/(Body1.position[1] - Body2.position[1])
        CosZV = Distance/(Body1.position[2] - Body2.position[2])