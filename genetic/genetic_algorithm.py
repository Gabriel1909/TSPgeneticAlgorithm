from genetic.genetic_operators import select, recombine, mutate, mutate_multiple, mutate_inversion
from problem.utils import plot_graph


def genetic_algorithm(population, fn_fitness, fn_thres=None, ngen=1000, pmut=0.1):
    results = []

    # for each generation
    for geration in range(ngen):

        # create a new population
        new_population = []

        # repeat to create len(population) individuals
        while len(new_population) < len(population):
            # select the parents
            p1, p2 = select(2, population, fn_fitness)

            # recombine the parents, thus producing the child
            child = recombine(p1, p2)

            # mutate the child
            child = mutate_inversion(child, pmut)

            if child in new_population:
                continue

            if fn_fitness(child) > (fn_fitness(p1) + fn_fitness(p2)) / 2:
                new_population.append(child)

        # move to the new population
        population = new_population

        print(geration)
        # check if one of the individuals achieved a fitness of fn_thres; if so, return it
        fittest_individual = fitness_threshold(fn_fitness, fn_thres, population, results)

        if fittest_individual:
            plot_graph(results)
            return fittest_individual

    # plot results
    plot_graph(results)

    # return the individual with highest fitness
    return max(population, key=fn_fitness)


# get the best individual of the received population and return it if its
# fitness is higher than the specified threshold fn_thres
def fitness_threshold(fn_fitness, fn_thres, population, results):
    if not fn_thres:
        return None

    fittest_individual = max(population, key=fn_fitness)
    result = fn_fitness.number - fn_fitness(fittest_individual)

    results.append(result)

    if result <= fn_thres:
        return fittest_individual

    return None
