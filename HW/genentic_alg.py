import GA


# Step 1 - Initialize Population
myPop = GA.Population(populationSize = 20, numGenes = 20)

for c in myPop.members:
    GA.myFitnessFunction(c)

# Step 2 - Selection
# Supose we selected Chrom 1 and 5

# Step 3 - Crossover and Mutate
# Crossover will generate new Chromosomes and will look like:
# newChrom = myPop[1] + myPop[5]

# Mutation will look like this, but only a small percent of the
# population Chromosomes will be mutated:
# newChrom.mutate()

# Step 4 - repeat
