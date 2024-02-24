# HW2 : Modified Brute-Force and Generic Algorithms
# By : Noah Fabrick

import random

values = [23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10]
weights = [7, 2, 6, 9, 1, 5, 6, 1, 3, 4, 7, 9, 3, 7, 3, 4, 5, 1, 5, 4]
pairs = []
for i in range(len(values)):
    pairs.append((weights[i],values[i]))


# MBFA
def MBFA_knapsack(pairs, maxWeight):
    pairsCopy = pairs.copy() # Copy pairs, had issues with pairs being deleted upon iteration
    # Initialize return variables
    knapsack = [] 
    ksWeight = 0
    ksValue = 0
    attempts = 0
    while True:
        attempts += 1
        i = random.randint(0,len(pairsCopy)-1)
        if pairsCopy[i][0] + ksWeight <= maxWeight:
            # if random item can be added to ks
            attempts = 0
            knapsack.append(pairsCopy[i]) # add item to knapsack
            ksWeight += pairsCopy[i][0] # add item weight to total weight 
            ksValue += pairsCopy[i][1] # add item value to total value
            pairsCopy.pop(i) # remove chosen item from possible options
        elif ksWeight == maxWeight:
            # Break when max weight is reached
            break
        elif attempts < len(pairsCopy)+1:
            # Give chance for all pairs to be tried
            pass
        else:
            # Break when too many attempts, avoids inf loops
            break

    return knapsack, ksWeight, ksValue

maxWeight = 45
N = 0
ksInvs = []
ksWeights = []
ksValues = []
while N < 50:
    N += 1
    knapsack_i, ksWeight_i, ksValue_i = MBFA_knapsack(pairs, 45)
    ksInvs.append(knapsack_i)
    ksWeights.append(ksWeight_i)
    ksValues.append(ksValue_i)
print('Modified Brute Force Algorithm Results after 50 attempts (weight [kg],value [$]):')
best1 = ksValues.index(max(ksValues))
print('1st Best Weight:',ksWeights[best1],'  1st Best Value:',ksValues[best1])
print('1st Best Inventory:',ksInvs[best1])
ksWeights.pop(best1)
ksValues.pop(best1)
ksInvs.pop(best1)
best2 = ksValues.index(max(ksValues))
print('2nd Best Weight:',ksWeights[best2],'  2nd Best Value:',ksValues[best2])
print('2nd Best Inventory:',ksInvs[best2])
ksWeights.pop(best2)
ksValues.pop(best2)
ksInvs.pop(best2)
best3 = ksValues.index(max(ksValues))
print('3rd Best Weight:',ksWeights[best3],'  3rd Best Value:',ksValues[best3])
print('3rd Best Inventory:',ksInvs[best3])