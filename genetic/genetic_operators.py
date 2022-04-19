import random as random
import bisect


# genetic operator for selection of individuals;
# this function implements roulette wheel selection, where individuals with
# higher fitness are selected with higher probability
def select(r, population, fn_fitness):
    fitnesses = map(fn_fitness, population)
    sampler = weighted_sampler(population, fitnesses)
    return [sampler() for _ in range(r)]


# return a single sample from seq; the probability of a sample being returned
# is proportional to its weight
def weighted_sampler(seq, weights):
    totals = []
    for w in weights:
        totals.append(w + totals[-1] if totals else w)
    return lambda: seq[bisect.bisect(totals, random.uniform(0, totals[-1]))]


# genetic operator for recombination (crossover) of individuals;
# this function implements single-point crossover, where the resulting individual
# carries a portion [0,c] from parent x and a portion [c,n] from parent y, with
# c selected at random
def recombine(x, y):
    n = len(x)
    c = random.randrange(0, n)
    return x[:c] + y[c:]


# genetic operator for mutation;
# this function implements uniform mutation, where a single element of the
# individual is selected at random and its value is changed by a randomly chosen
# value (out of the possible values in gene_pool)
def mutate(x, gene_pool, pmut):
    # if random >= pmut, then no mutation is performed
    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)
    g = len(gene_pool)
    c = random.randrange(0, n)  # gene to be mutated
    r = random.randrange(0, g)  # new value of the selected gene

    new_gene = gene_pool[r]
    return x[:c] + [new_gene] + x[c + 1:]
