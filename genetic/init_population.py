import random as random


def init_population(pop_number, gene_pool, state_length):
    g = len(gene_pool)
    population = []
    for _ in range(pop_number):
        # each individual is represented as an array with size state_length,
        # where each position contains a value from gene_pool selected at random
        while True:
            new_individual = [gene_pool[random.randrange(0, g)] for _ in range(state_length)]

            if population.__contains__(new_individual):
                continue

            population.append(new_individual)
            break

    return population
