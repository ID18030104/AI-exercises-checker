import random


class Gene:
    def __init__(self):
        self.value = random.choice([0, 1])

    def mutate(self):
        self.value = 1 - self.value  
    
    def __str__(self):
        return str(self.value)



class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]

    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.5:  
                gene.mutate()

    def is_full_of_ones(self):
        return all(gene.value == 1 for gene in self.genes)

    def __str__(self):
        return ''.join(str(gene) for gene in self.genes)



class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]

    def mutate(self):
        for chromosome in self.chromosomes:
            chromosome.mutate()

    def is_full_of_ones(self):
        return all(chromosome.is_full_of_ones() for chromosome in self.chromosomes)

    def __str__(self):
        return '\n'.join(str(chromosome) for chromosome in self.chromosomes)



class Organism:
    def __init__(self, dna: DNA, environment: float):
        self.dna = dna
        self.environment = environment  

    def mutate(self):
        if random.random() < self.environment:
            self.dna.mutate()


def simulate_until_perfection(environment_probability):
    generations = 0
    dna = DNA()
    organism = Organism(dna, environment_probability)

    while not organism.dna.is_full_of_ones():
        organism.mutate()
        generations += 1

    return generations, organism.dna


if __name__ == "__main__":
    env = 0.9  
    generations, final_dna = simulate_until_perfection(env)

    print(f"✅ DNA perfection achieved after {generations} generations.\n")
    print("🧬 Final DNA:")
    print(final_dna)