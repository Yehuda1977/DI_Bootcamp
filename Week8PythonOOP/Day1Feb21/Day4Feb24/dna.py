"""
This challenge is about Biology.

Build a DNA object. DNA is composed of chromosomes which is itself composed of Genes.

A Gene is a single value 0 or 1, it can mutate (flip).
A Chromosome is a series of 10 Genes. It also can mutate, meaning a random number of genes can randomly flip
(1/2 chance to flip).
A DNA is a series of 10 chromosome, and it can also mutate the same way Chromosomes can.
Implement these classes as you see fit.

Create a new class called Organism that accepts a DNA object and a environement parameter that sets the probability for
its DNA to mutate.
Instantiate a number of Organims and let them mutate until one gets to a DNA is only made of 1s. Then stop and record
the number of generations (iterations) it took.
Write your results in you personal biology research notebook and tell us your conclusion :).
"""

import random
# To get a random number between a and b, just use random.randint(a,b)

class Gene:
    def __init__(self, value=0):
        self.value = value

    def flip(self):
        if self.value == 1:
            self.value = 0
        else:
            self.value = 1


class Chromosome:
    def __init__(self, genes):
        """
        :param genes: A list of 10 Gene objects
        """
        self.genes = genes

    def mutate(self):
        for gene in self.genes:
            if random.randint(0,1) == 0: # 1/2 chance to be 0
                gene.flip()

    @classmethod # Decorator
    def get_random_chromosome(cls):
        """
        1) There is no 'self' parameter anymore
        2) It's replaced by 'cls' parameter that contains the class itself (Chromosome)
        :return:
        """
        genes = []  # The genes that compose the chromosome
        i = 0
        while i <= 10:  # Genes creator
            gene = Gene(random.randint(0, 1))
            genes.append(gene)

            i += 1
        # Instead of:
        # chromosome = Chromosome(genes)
        # Use:
        chromosome = cls(genes)
        return chromosome

class DNA:
    def __init__(self, chromosomes):
        """

        :param chromosomes: A list of 10 Chromosome objects
        """
        self.chromosomes = chromosomes

    def mutate(self):
        for chromosome in self.chromosomes:
            if random.randint(0,1) == 0: # 1/2 chance to be 0
                chromosome.mutate()


class Organism:

    def __init__(self, dnas, mutate_prob):
        self.dnas = dnas
        self.mutate_prob = mutate_prob

    def mutate(self):
        for dna in self.dnas:
            if random.randint(0,100) <= self.mutate_prob:
                dna.mutate()




def get_random_dna():
    chromosomes = []

    i = 0
    while i <= 10: #Chromosomes creator
        chromosome = Chromosome.get_random_chromosome()
        chromosomes.append(chromosome)
        i += 1

    dna = DNA(chromosomes)
    return dna

def get_random_organism():
    dnas = []
    i = 0
    while i <= 10: #DNA creator
        dna = get_random_dna()
        dnas.append(dna)
        i+=1
                            # vvv random mutate_prob
    organism = Organism(dna, random.randint(0,100))
    return organism

organism = get_random_organism()

print(organism)






