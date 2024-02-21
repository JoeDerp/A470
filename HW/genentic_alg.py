import GA
import random

values = [23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10]
weights = [7, 2, 6, 9, 1, 5, 6, 1, 3, 4, 7, 9, 3, 7, 3, 4, 5, 1, 5, 4]

# Step 1 - Initialize Population
myPop = GA.Population(populationSize = 20, numGenes = 20)

print([Chrom.fitness for Chrom in myPop.members])

for i in range(2):
    for c in myPop.members:
        GA.myFitnessFunction(c,values,weights)

    # Step 2 - Selection
    # Supose we selected Chrom 1 and 5
    selection = myPop.selection(0.5)
    # Step 3 - Crossover and Mutate 
    # Crossover will generate new Chromosomes and will look like:
    randCross = random.randint(2,len(selection)-1)
    selection.extend(selection[0] + selection[randCross])
    newRandCross = random.randint(2,len(selection)-1)
    selection.extend(selection[1] + selection[newRandCross])
    selection.extend(selection[0]+selection[1])


    # Mutation will look like this, but only a small percent of the
    # population Chromosomes will be mutated:
    # newChrom.mutate()
    randMutate = random.randint(0,len(selection)-1)
    newRandMutate = random.randint(0,len(selection)-1)
    selection.append(selection[randMutate].mutate())
    selection.append(selection[newRandMutate].mutate())

    # Step 4 - repeat
    myPop.members = selection

print([Chrom.fitness for Chrom in myPop.members])
