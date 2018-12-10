import numpy as np
class TractorBeam(object):
    def __init__(self, Emitter, Receiver, Force):
        self.Emitter = Emitter
        self.Receiver = Receiver
        self.Force = Force
    def Update(self):
        Distance = np.sqrt((self.Emitter.position[0] - self.Receiver.position[0])^2 + (self.Emitter.position[1] - self.Receiver.position[1])^2 + (self.Emitter.position[2] - self.Receiver.position[2]^2))
        CosXV = (self.Emitter.position[0] - self.Receiver.position[0])/Distance
        CosYV = (self.Emitter.position[1] - self.Receiver.position[1])/Distance
        CosZV = (self.Emitter.position[2] - self.Receiver.position[2])/Distance
        
        Gravity = ((self.Force*self.Emitter.mass*1000)*(self.Receiver.mass*1000))/(Distance^2)
        #ACTION...
        self.Emitter.vel[0] = self.Emitter.vel[0]*(Gravity/(self.Emitter.mass*1000)*CosXV)
        self.Emitter.vel[1] = self.Emitter.vel[1]*(Gravity/(self.Emitter.mass*1000)*CosYV)
        self.Emitter.vel[2] = self.Emitter.vel[2]*(Gravity/(self.Emitter.mass*1000)*CosZV)
        #...AND REACTION
        self.Receiver.vel[0] = self.Receiver.vel[0]*-(Gravity/(self.Receiver.mass*1000)*CosXV)
        self.Receiver.vel[1] = self.Receiver.vel[1]*-(Gravity/(self.Receiver.mass*1000)*CosYV)
        self.Receiver.vel[2] = self.Receiver.vel[2]*-(Gravity/(self.Receiver.mass*1000)*CosZV)