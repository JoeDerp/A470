# Classes for Goose object to be used for V-Formation ALgorithm
# By: Noah Fabrick

import numpy as np

class Goose:

    def __init__(self,x,a,ch):
        self.x = x # position of goose [x,y]
        self.width = [x[0]-a,x[0]+a] # goose physical width given a
        self.height = [x[1]-(ch/2),x[1]+(ch/2)] # goose physical length given ch
        self.d_nom = np.sqrt((2*a)**2 + (a*(1.1+(np.pi/4)))**2) # goose far-field radius
        self.lead_i = 0 # initialize index of bird in front
        self.rHat = 0 # initialize rHat, the following vector

class Geese:

    def __init__(self,size,a,ch):
        self.pop = []
        self.global_i = 0
        for i in range(size):
            x = np.random.uniform(0,size*2,2)
            self.pop.append(Goose(x,a,ch))

    def findLead(self):
        for i in range(len(self.pop)):
            ahead = [g for g in self.pop if g.x[1] > self.pop[i].x[1]] # create list of geese with higher y-value than goose_i
            if not ahead: # if list of geeese ahead is empty, self is the lead goose
                self.pop[i].lead_i = i
                self.global_i = i
            else: # else, find closest goose from list of geese ahead
                ahead_y = [goose.x[1] for goose in ahead]
                leadGoose = ahead[ahead_y.index(min(ahead_y))]
                self.pop[i].lead_i = self.pop.index(leadGoose)
        return self

    def rHats(self):
        for goose in self.pop:
            goose.rHat = [[goose.x[0]-(goose.d_nom/2),goose.x[1]-(goose.d_nom/2)],[goose.x[0]+(goose.d_nom/2),goose.x[1]+(goose.d_nom/2)]] # One rHat vector pointing backwards and left and one pointing backwards and right

    def updatePos(self,dt):
        for g in self.pop:
            if self.pop.index(g) == self.global_i: # Global Lead
                g.x[1] += dt # Just move forward
            else:
                if np.linalg.norm(np.array([g.x[0]-self.pop[g.lead_i].x[0],g.x[1]-self.pop[g.lead_i].x[1]])) >= g.d_nom: # Far-Field
                    r = np.array([self.pop[g.lead_i].x[0]-g.x[0],self.pop[g.lead_i].x[1]-g.x[1],]) # Head to lead goose
                    g.x[0] += (r[0]/np.linalg.norm(r))*dt
                    g.x[1] += (r[1]/np.linalg.norm(r))*dt
                else: # Near Field
                    if g.x[0] < self.pop[self.global_i].x[0]: # If left of global lead
                        r = np.array([self.pop[g.lead_i].rHat[0][0]-g.x[0],self.pop[g.lead_i].rHat[0][1]-g.x[1],]) # go to leader's left rHat
                        g.x[0] += (r[0]/np.linalg.norm(r))*dt
                        g.x[1] += (r[1]/np.linalg.norm(r))*dt
                    else:
                        r = np.array([self.pop[g.lead_i].rHat[1][0]-g.x[0],self.pop[g.lead_i].rHat[1][1]-g.x[1],]) # go to leader's right rHat
                        g.x[0] += (r[0]/np.linalg.norm(r))*dt
                        g.x[1] += (r[1]/np.linalg.norm(r))*dt

