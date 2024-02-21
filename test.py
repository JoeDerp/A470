class CustomMath:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        # Override the addition operator to multiply instead
        return CustomMath(self.num * other)

    def square(self):
        # Define a custom method to square the number
        return self.num ** 2

    def cube(self):
        # Define a custom method to cube the number
        return self.num ** 3
    
    def power(self, exp):
        # Define a custom method to cube the number
        self.num = self.num ** exp
        return self.num

# Example usage:
num_obj = CustomMath(5)
newNum = num_obj + 2
print(newNum.num)  # Output will be 10, because __add__ is overridden
print(num_obj.square())  # Output will be 25
print(num_obj.cube())    # Output will be 125
print(num_obj.power(4))    # Output will be 125
print(newNum.square())