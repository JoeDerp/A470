# By: Noah Fabrick
import numpy as np
import matplotlib.pyplot as plt
        
class Server:

    def __init__(self):
        self.isBusy = False # indicator if server is busy, boolean value initially set to False (not busy)
        self.timeDone = float('inf') # time till current customer is finished being serviced

class Restaurant:

    def __init__(self, numServers, serviceTime,avgServTime):
        # System Initialization
        self.staff = [Server() for i in range(numServers)]
        self.serviceTimes = []
        self.relArrTimes = []
        self.generateCustomers(serviceTime,avgServTime)
        # System State
        self.queueN = 0 # general waiting queue
        self.queue = [] # service queue of customers awaiting server
        # Statistical Counters
        self.numArrivals = 0
        self.numDepartures = 0
        self.totalWait = 0
        # Simulation Variables
        self.clock = 0
        self.nextArrival = 0

    def generateCustomers(self,serviceTime,avgServTime):
        while sum(self.relArrTimes)<=serviceTime:
            self.relArrTimes.append(np.random.exponential(1./3))
            self.serviceTimes.append(np.random.exponential(avgServTime))
        self.relArrTimes.pop() # Customers can't come in after close
        self.serviceTimes.pop()
        return self

    def openRestaurant(self):
        self.nextArrival = self.relArrTimes[0] # set next arrival time
        return self
        
    def advanceTime(self):
        while self.relArrTimes or self.queue: # if more customers need to arrive/be served
            nextEvents = [server.timeDone for server in self.staff]
            nextEvents.append(self.nextArrival)
            tNextEvent = min(nextEvents)
            tInt = tNextEvent-self.clock
            self.clock += tInt
            if self.queueN > 0:
                self.totalWait += tInt*self.queueN
            if tNextEvent == self.nextArrival:
                self.handleArrival()
                self.handleService()
            else:
                self.handleDeparture(nextEvents.index(tNextEvent))
                self.handleService()
        else:
            return self

    def handleArrival(self):
        self.relArrTimes.pop(0) # the next customer has arrived
        self.numArrivals += 1
        self.queueN += 1
        self.queue.append(self.serviceTimes.pop(0)) # customer joins service queue with their respective service time
        if self.relArrTimes:
            self.nextArrival += self.relArrTimes[0] # set next arrival time
        else:
            self.nextArrival = float('inf')
        return self

    def handleService(self):
        for cust in self.queue: # for every customer waiting for a server
            serverFound = False
            for server in self.staff: # check every server
                if not server.isBusy: # if server not busy
                    serverFound = True # cust has found server
                    server.isBusy = True # set server to busy
                    server.timeDone = cust + self.clock # set server's service time
                    self.queue.remove(cust) # remove cust from service queue
                    break
            if not serverFound: # if all servers are busy
                return self

    def handleDeparture(self,i):
        self.queueN -= 1
        self.numDepartures += 1
        self.staff[i].isBusy = False
        self.staff[i].timeDone = float('inf')
        return self

    def closeRestaurant(self):
        while self.numArrivals > self.numDepartures: # finish serving last customers
            nextEvents = [server.timeDone for server in self.staff]
            nextEvents.append(self.nextArrival)
            tNextEvent = min(nextEvents)
            tInt = tNextEvent-self.clock
            self.clock += tInt
            if self.queueN > 0:
                self.totalWait += tInt*self.queueN
            self.handleDeparture(nextEvents.index(tNextEvent))
        # printout of the day
        print(self.numArrivals, 'customers arrived at the restaurant')
        print(self.numDepartures, 'customers departed from the restaurant')
        print('The final clock was',self.clock)
        print('The total wait time was',self.totalWait)

# tSpan = 60*5 # 5 hours of service
# avgServTime = 1./4
# numStaff = 5 # 5 servers
# chipotle = Restaurant(numStaff,tSpan)
# chipotle.openRestaurant()
# chipotle.advanceTime()
# chipotle.closeRestaurant()
        
tSpans = [(i+1)*60 for i in range(10)] # service windows of 1 to 10 hours, in minutes
avgServTime1 = 1./4
numStaff1 = 1
waitTimes = []
numCusts = []
for t in tSpans:
    rest = Restaurant(numStaff1,t,avgServTime1)
    rest.openRestaurant()
    rest.advanceTime()
    rest.closeRestaurant()
    waitTimes.append(rest.totalWait)
    numCusts.append(rest.numDepartures)
fig1,ax1 = plt.subplots()
ax1.plot([t/60 for t in tSpans], waitTimes,'b*')
ax1.set_title('Day Statistics for Restaurant')
ax1.set_xlabel('Service Window [hr]')
ax1.set_ylabel('Total Wait Time [min]', color='b')
ax1.grid('True')
ax2 = ax1.twinx()
ax2.plot([t/60 for t in tSpans], numCusts,'r*')
ax2.set_ylabel('# of Customers Served', color='r')

plt.show()