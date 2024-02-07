import numpy as np
import random

class Chromosome:

    def __init__(self, numGenes = 20):
        self.genes = random.choices([0, 1], k = numGenes)
        self.fitness = 0

    def mutate():
        # Implement random mutation
        pass

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

def myFitnessFunction(chrom: Chromosome):
    # chrom.fitness = some function of chrom.genes
    pass