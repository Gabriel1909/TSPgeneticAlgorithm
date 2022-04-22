import random as random
import bisect

from problem.utils import swap


# genetic operator for selection of individuals;
# this function implements roulette wheel selection, where individuals with
# higher fitness are selected with higher probability
def select(r, population, fn_fitness):
    fitnesses = map(fn_fitness, population)
    sampler = weighted_sampler(population, fitnesses)
    return [sampler() for _ in range(r)]


def select_best(r, population, fn_fitness):
    fitnesses = map(fn_fitness, population)

    selection = list()
    fitnesses_list = list(fitnesses)
    for i in range(r):
        index = fitnesses_list.index(max(fitnesses_list))
        fitnesses_list.remove(max(fitnesses_list))
        selection.append(population[index])

    return selection


# return a single sample from seq; the probability of a sample being returned
# is proportional to its weight
def weighted_sampler(seq, weights):
    totals = []
    for w in weights:
        totals.append(w + totals[-1] if totals else w)
    return lambda: seq[bisect.bisect(totals, random.uniform(0, totals[-1]))]


def recombine_ox(x, y):
    n = len(x)

    minimo = 30
    maximo = 40

    primeiro_corte = random.randrange(0, n-maximo)

    segundo_corte = primeiro_corte + random.randrange(minimo, maximo)

    resultado = [-1 for _ in range(0, n)]

    resultado[primeiro_corte:segundo_corte] = x[primeiro_corte:segundo_corte]

    valores_validos = x[0:primeiro_corte] + x[segundo_corte:n]

    index_y = n-1

    for index in range(n-1, -1, -1):
        if resultado[index] == -1:

            while True:
                if y[index_y] in valores_validos:
                    resultado[index] = y[index_y]
                    index_y -= 1
                    break
                else:
                    index_y -= 1

    return resultado


def recombine_cx(x, y):
    curr = 0  # starts at 0

    cycle = {  # index: value
        curr: x[curr],
    }

    curr = y[curr]
    while curr not in list(cycle.keys()):
        cycle[curr] = x[curr]
        curr = y[curr]

    resultado = [-1] * len(x)

    for i, value in cycle.items():
        resultado[i] = value

    remaining_values = list(set(y) - set(resultado))

    for i in range(len(resultado)):
        if resultado[i] == -1:
            resultado[i] = remaining_values.pop(0)

    return resultado


def mutate(x, pmut):

    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)
    c = random.randrange(0, n)
    r = random.randrange(0, n)
    swap(x, c, r)

    return x


def mutate_multiple(x, pmut):

    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)
    mut_factor = 0.1
    swaps = int(n * mut_factor) if int(n * mut_factor) != 0 else 1

    for i in range(swaps):
        c = random.randrange(0, n)
        r = random.randrange(0, n)
        swap(x, c, r)

    return x


def mutate_inversion(x, pmut):

    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)
    i = random.randrange(0, n)
    j = random.randrange(i, n)

    temp = x[i:j]
    temp.reverse()
    x[i:j] = temp

    return x
