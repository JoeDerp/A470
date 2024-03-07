# Classes for Goose object to be used for V-Formation ALgorithm
# By: Noah Fabrick

import numpy as np

class Goose:

    def __init__(self,x,a,ch):
        self.x = x # position of goose [x,y]
        self.width = [x[0]-a,x[0]+a] # goose physical width given a
        self.height = [x[1]-(ch/2),x[1]+(ch/2)] # goose physical length given ch
        self.d_nom = np.sqrt((2*a)**2 + (a*(1.1+(np.pi/4)))**2) # goose far-field radius

    def findLead(self,geese):
        ahead = [goose for goose in geese if goose.x[1] > self.x[1]] # create list of geese with higher y-value than self goose
        if not ahead: # if list of geeese ahead is empty, self is the lead goose
            self.lead_i = geese.index(self)
            return self
        else: # else, find closest goose from list of geese ahead
            ahead_y = [goose.x[1] for goose in ahead]
            leadGoose = ahead[ahead_y.index(min(ahead_y))]
            self.lead_i = geese.index(leadGoose)
            return self

    def updateX(self,geese):
        pass

    def updateY(self,geese):
        pass

# g = [Goose([5,5],0.2,0.1),Goose([1,9],0.2,0.1),Goose([15,8],0.2,0.1)]
# g[1].findLead(g)
# print(g[1].lead_i)