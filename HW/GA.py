import numpy as np
import random

class Chromosome:

    def __init__(self, numGenes = 20):
        self.genes = random.choices([0, 1], k = numGenes)
        self.fitness = 0

    def mutate(self):
        # Implement random mutation
        randGene = random.randint(0,len(self.genes)-1)
        if self.genes[randGene] == 0:
            self.genes[randGene] = 1
        else:
            self.genes[randGene] = 0
        return self.genes

    def __add__(self, o):
        # Implement single point crossover with random crossover point

        pass

class Population:

    def __init__(self, populationSize, numGenes = 20):
        self.members = [Chromosome(numGenes) for i in range(populationSize)]

    def selection(self, ratio):
        # Implement Selection
        # Step 1 - Sort members by fitness
        self.members.sort(key=lambda x:x.fitness)
        # Step 2 - return some number of members based on the ratio provided

def myFitnessFunction(chrom: Chromosome, vals, weights):
    value = 0
    weight = 0
    i = 0
    for gene in chrom.genes:
        if gene == 1:
            value += vals[i]
            weight += weights[i]
        i += 1
    if weight <= 45:
        wFactor = 0
    else:
        wFactor = -150
    
    chrom.fitness = value + wFactor
    return chrom.fitness

print(sum([23, 21, 8, 1, 3, 7, 18, 19, 17, 15, 24, 22, 6, 28, 4, 2, 27, 20, 5, 10]))