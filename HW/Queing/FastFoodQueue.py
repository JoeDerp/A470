# By: Noah Fabrick
import numpy as np

class Customer:

    def __init__(self, maxArrivalTime, avgServiceTime):
        self.arrivalTime = np.random.uniform(0,maxArrivalTime+np.finfo(float).eps) # np.finfo(float).eps is smallest representable number, so creates arrival time on range [0,closing time]
        stdServiceTime = 1
        self.serviceTime = np.random.normal(avgServiceTime,stdServiceTime)
        while self.serviceTime <= 0:
            # service time can't be 0 or less seconds
            self.serviceTime = np.random.normal(avgServiceTime,stdServiceTime)
        
class Server:

    def __init__(self):
        self.isBusy = False # indicator if server is busy, boolean value initially set to False (not busy)
        self.timeDone = float('inf') # time till current customer is finished being serviced

class Restaurant:

    def __init__(self, numServers, numCustomers, maxArrivalTime, avgServiceTime):
        # System Initialization
        self.staff = [Server() for i in range(numServers)]
        self.customers = [Customer(maxArrivalTime,avgServiceTime) for i in range(numCustomers)]
        self.customers.sort(key=lambda cust: cust.arrivalTime)
        self.serviceTimes = [cust.serviceTime for cust in self.customers]
        arrivalTimes = [cust.arrivalTime for cust in self.customers]
        self.relArrivalTimes = [arrivalTimes[0]]
        for i in range(1,len(arrivalTimes)):
            self.relArrivalTimes.append(arrivalTimes[i]-arrivalTimes[i-1])
        # System State
        self.queue = 0
        # Statistical Counters
        self.numArrivals = 0
        self.numDepartures = 0
        self.totalWait = 0
        # Simulation Variables
        self.clock = 0
        self.nextArrival = 0

    def openRestaurant(self):
        self.nextArrival = self.relArrivalTimes[0] # set next arrival time
        return self
        
    def advanceTime(self):
        nextEvents = [server.timeDone for server in self.staff]
        nextEvents.append(self.nextArrival)
        t_event = min(nextEvents)
        self.clock += t_event-self.clock

        # add if statement to check if out of time range

        if t_event == min(self.nextArrival):
            self.handleArrival()
        else:
            self.handleDeparture()
        return self

    def handleArrival(self):
        self.queue += 1
        self.relArrivalTimes.pop(0)


    def handleDeparture(self):
        pass
