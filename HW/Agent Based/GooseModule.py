# Classes for Goose object to be used for V-Formation ALgorithm
# By: Noah Fabrick

import numpy as np

class Goose:

    def __init__(self,x,a,ch):
        self.x = x # position of goose [x,y]
        self.width = [x[0]-a,x[0]+a] # goose physical width given a
        self.height = [x[1]-(ch/2),x[1]+(ch/2)] # goose physical length given ch
        self.d_nom = np.sqrt((2*a)**2 + (a*(1.1+(np.pi/4)))**2) # goose far-field radius
        # find if goose is in left or right field, -x or +x respectively (0 is pos)
        if x[0] < 0:
            self.r_l = 'l'
        else:
            self.r_l = 'r'
        self.lead_i = None # initialize index of bird in front
        self.rHats = None # initialize following vectors

class Geese:

    def __init__(self,size,a,ch,r):
        # Generate population of Goose objects 
        self.pop = []
        for i in range(size):
            x = np.random.uniform(r[0]+np.finfo(float).eps,r[1],2) # x = [x_i,y_i] which a randomly generated values within range
            self.pop.append(Goose(x,a,ch))
        self.popLead = None 
        self.rightLead = None # initialize indexes of population, rightfield, and leftfield leads
        self.leftLead = None

    def findLeads(self):
        # find index of population's lead goose
        yVals = [g.x[1] for g in self.pop]
        self.popLead = yVals.index(max(yVals)) # index of goose with highest y-value is lead
        self.pop[self.popLead].lead_i = self.popLead # population lead goose's lead is itself
        # sort population by right/left field, excluding popLead
        right = [g for g in self.pop if g.r_l == 'r' and g.lead_i != self.popLead]
        left = [g for g in self.pop if g.r_l == 'l' and g.lead_i != self.popLead]
        for g_r in right:
            # find goose with next highest y-value on rightfield
            ahead = [g for g in right if g.x[1] > g_r.x[1]]
            if not ahead: # if list of geeese ahead is empty, self is the rightfield lead goose
                self.rightLead = self.pop.index(g_r)
                g_r.lead_i = self.popLead
            else: # else, find closest goose from list of geese ahead
                ahead_y = [goose.x[1] for goose in ahead]
                leadGoose = ahead[ahead_y.index(min(ahead_y))] # the min y-value is the next highest goose
                g_r.lead_i = self.pop.index(leadGoose)
        for g_l in left:
            # find goose with next highest y-value on leftfield
            ahead = [g for g in left if g.x[1] > g_l.x[1]]
            if not ahead: # if list of geeese ahead is empty, self is the leftfield lead goose
                self.leftLead = self.pop.index(g_l)
                g_l.lead_i = self.popLead
            else: # else, find closest goose from list of geese ahead
                ahead_y = [goose.x[1] for goose in ahead]
                leadGoose = ahead[ahead_y.index(min(ahead_y))] # the min y-value is the next highest goose
                g_l.lead_i = self.pop.index(leadGoose)
        return self

    def rHat(self):
        for goose in self.pop:
            # One rHat vector pointing backwards and left and one pointing backwards and right
            goose.rHats = [[goose.x[0]-(goose.d_nom/(2*np.sqrt(2))),goose.x[1]-(goose.d_nom/(2*np.sqrt(2)))],[goose.x[0]+(goose.d_nom/(2*np.sqrt(2))),goose.x[1]-(goose.d_nom/(2*np.sqrt(2)))]]
        return self

    def updatePos(self,dx):
        for g in self.pop:
            if self.pop.index(g) == self.popLead: # population lead
                r = np.array([0-g.x[0],0.05]) # move forwards and towards center (x=0)
                g.x[0] += (r[0]/np.linalg.norm(r))*dx
                g.x[1] += (r[1]/np.linalg.norm(r))*dx 
            else:
                if np.linalg.norm(np.array([g.x[0]-self.pop[g.lead_i].x[0],g.x[1]-self.pop[g.lead_i].x[1]])) >= g.d_nom: # Far-Field
                    r = np.array([self.pop[g.lead_i].x[0]-g.x[0],self.pop[g.lead_i].x[1]-g.x[1],]) # Head to lead goose
                    g.x[0] += (r[0]/np.linalg.norm(r))*dx
                    g.x[1] += (r[1]/np.linalg.norm(r))*dx
                else: # Near Field
                    if g.r_l == 'l': # If in leftfield
                        # go to leader's leftward rHat
                        r = np.array([self.pop[g.lead_i].rHats[0][0]-g.x[0],self.pop[g.lead_i].rHats[0][1]-g.x[1],])
                        g.x[0] += (r[0]/np.linalg.norm(r))*dx
                        g.x[1] += (r[1]/np.linalg.norm(r))*dx
                    else:
                        # go to leader's rightward rHat
                        r = np.array([self.pop[g.lead_i].rHats[1][0]-g.x[0],self.pop[g.lead_i].rHats[1][1]-g.x[1],])
                        g.x[0] += (r[0]/np.linalg.norm(r))*dx
                        g.x[1] += (r[1]/np.linalg.norm(r))*dx
        return self

