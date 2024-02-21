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
        return self

    def __add__(self, o):
        # Implement single point crossover with random crossover point
        newSelf = Chromosome(numGenes = 20)
        newO = Chromosome(numGenes = 20)
        randPoint = random.randint(1,len(self.genes)-1)
        newSelf.genes = list(self.genes[0:randPoint])
        newSelf.genes.extend(o.genes[randPoint:len(self.genes)])
        newO.genes = list(o.genes[0:randPoint])
        newO.genes.extend(self.genes[randPoint:len(self.genes)])
        crossed = [newSelf, newO]
        return crossed

class Population:

    def __init__(self, populationSize, numGenes = 20):
        self.members = [Chromosome(numGenes) for i in range(populationSize)]

    def selection(self, ratio):
        # Implement Selection
        # Step 1 - Sort members by fitness
        self.members.sort(key=lambda x:x.fitness)
        # Step 2 - return some number of members based on the ratio provided
        selection = []
        for i in range(int(len(self.members)*ratio),len(self.members)):
            selection.append(self.members[i])
        return selection

        
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

