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
        print('The final clock was',round(self.clock,2),'min')
        print('The total wait time was',round(self.totalWait,2),'min')

tSpan = 60*5 # 5 hours of service
avgServTime = 1./4
numStaff = 1 # 1 server
chipotle = Restaurant(numStaff,tSpan,avgServTime)
chipotle.openRestaurant()
chipotle.advanceTime()
chipotle.closeRestaurant()
        
# tSpans = [(i+1)*60 for i in range(10)] # service windows of 1 to 10 hours, in minutes
# avgServTime1 = 1./4
# numStaff1 = 1
# waitTimes = []
# numCusts = []
# for t in tSpans:
#     rest = Restaurant(numStaff1,t,avgServTime1)
#     rest.openRestaurant()
#     rest.advanceTime()
#     rest.closeRestaurant()
#     waitTimes.append(rest.totalWait)
#     numCusts.append(rest.numDepartures)
# fig1,ax1 = plt.subplots()
# ax1.plot([t/60 for t in tSpans], waitTimes,'b*')
# ax1.set_title('Day Statistics for Restaurant')
# ax1.set_xlabel('Service Window [hr]')
# ax1.set_ylabel('Total Wait Time [min]', color='b')
# ax1.grid('True')
# ax2 = ax1.twinx()
# ax2.plot([t/60 for t in tSpans], numCusts,'r*')
# ax2.set_ylabel('# of Customers Served', color='r')


# tSpan3 = 10*60 # 10 hours
# avgServTime3 = 3 # 3 minutes average service time
# numServers = [i+1 for i in range(5)]
# waitTimes2 = []
# for ss in numServers:
#     for i in range(5):
#         rest = Restaurant(ss,tSpan3,avgServTime3)
#         rest.openRestaurant()
#         rest.advanceTime()
#         rest.closeRestaurant()
#         waitTimes2.append(rest.totalWait)

# fig3,ax3 = plt.subplots()
# ax3.plot([i+1 for i in range(5)], waitTimes2[0:5],'b',label='1 Server')
# ax3.plot([i+1 for i in range(5)], waitTimes2[5:10],'r',label='2 Servers')
# ax3.plot([i+1 for i in range(5)], waitTimes2[10:15],'g',label='3 Servers')
# ax3.plot([i+1 for i in range(5)], waitTimes2[15:20],'y',label='4 Servers')
# ax3.plot([i+1 for i in range(5)], waitTimes2[20:25],'rebeccapurple',label='5 Servers')
# ax3.set_title('Total Wait Time vs. Staff Size for 10hr Service')
# ax3.set_xlabel('Iteration')
# ax3.set_ylabel('Total Wait Time [min]')
# ax3.legend(fontsize = 'small')
# ax3.grid('True')
# plt.show()