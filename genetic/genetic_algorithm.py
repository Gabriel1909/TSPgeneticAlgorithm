from genetic.genetic_operators import select, recombine, mutate


def genetic_algorithm(population, fn_fitness, gene_pool, fn_thres=None, ngen=1000, pmut=0.1):
    # for each generation
    for i in range(ngen):

        # create a new population
        new_population = []

        # repeat to create len(population) individuals
        for j in range(len(population)):
            # select the parents
            p1, p2 = select(2, population, fn_fitness)

            # recombine the parents, thus producing the child
            child = recombine(p1, p2)

            # mutate the child
            child = mutate(child, gene_pool, pmut)

            # add the child to the new population
            new_population.append(child)

        # move to the new population
        population = new_population

        # check if one of the individuals achieved a fitness of fn_thres; if so, return it
        fittest_individual = fitness_threshold(fn_fitness, fn_thres, population)
        if fittest_individual:
            return fittest_individual

    # return the individual with highest fitness
    return max(population, key=fn_fitness)


# get the best individual of the received population and return it if its
# fitness is higher than the specified threshold fn_thres
def fitness_threshold(fn_fitness, fn_thres, population):
    if not fn_thres:
        return None

    fittest_individual = max(population, key=fn_fitness)
    if fn_fitness(fittest_individual) >= fn_thres:
        return fittest_individual

    return None
