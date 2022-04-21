import random as random
import copy


def init_population(pop_number, gene_pool):
    population = []

    for _ in range(pop_number):

        genes_validos = copy.deepcopy(gene_pool)
        new_individual = []

        while genes_validos:
            gene = genes_validos[random.randrange(0, len(genes_validos))]
            if gene in genes_validos:
                genes_validos.remove(gene)
                new_individual.append(gene)

        population.append(new_individual)

    return population
