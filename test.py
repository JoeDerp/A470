def selection(self, ratio):
    # Implement Selection
    # Step 1 - Sort members by fitness
    self.sort()
    # Step 2 - return some number of members based on the ratio provided
    selection = []
    for i in range(int(len(self)*ratio),len(self)):
        selection.append(self[i])
    return selection
# Example usage:

values = [23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10]

sorted = values.sort()
print(values)
print(selection(values,0.5))
