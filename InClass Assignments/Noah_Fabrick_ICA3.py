# By: Noah Fabrick

class transportation:
    def __init__(self,type,range,capacity):
        self.type = type
        self.range = range
        self.capacity = capacity

    def __str__(self):
        return f"The {self.type} can move up to {self.capacity} people a maximum distance of {self.range} miles."
    
    def __eq__(self,other):
        if self.range > other.range:
            return f"The {self.type} will take you further than the {other.type}"
        elif other.range > self.range:
            return f"The {other.type} will take you further than the {self.type}"
        else:
            return "Both transports will take you the same distance"

class cars(transportation):
    def __init__(self,type,range,capacity,make,model,color):
        super().__init__(type,range,capacity)
        self.make = make
        self.model = model
        self.color = color
    
    def whatColor(self):
        print("The",self.make,self.model,"is",self.color)

    def whatBrand(self):
        print("The",self.type,"is a",self.make,self.model)

class planes(transportation):
    def __init__(self,type,range,capacity,airline,make,model):
        super().__init__(type,range,capacity)
        self.airline = airline
        self.make = make
        self.model = model

    def __str__(self):
        return f"{self.airline}'s {self.make} {self.model} can move up to {self.capacity} people a maximum distance of {self.range} miles."
