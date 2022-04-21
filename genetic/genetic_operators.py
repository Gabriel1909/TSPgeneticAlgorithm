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


def recombine(x, y):
    n = len(x)

    corte_aleatorio = random.randrange(0, n)

    primeiro_intervalo = x[:corte_aleatorio]

    valores_validos = x[corte_aleatorio:]

    segundo_intervalo = y[corte_aleatorio:]

    for index in range(0, len(segundo_intervalo)):

        while segundo_intervalo[index] not in valores_validos:
            segundo_intervalo[index] = random.choice(valores_validos)

        valores_validos.remove(segundo_intervalo[index])

    return primeiro_intervalo + segundo_intervalo


def mutate(x, pmut):

    if random.uniform(0, 1) >= pmut:
        return x

    n = len(x)

    c = random.randrange(0, n)
    r = random.randrange(0, n)

    temp = x[c]

    x[c] = x[r]
    x[r] = temp

    return x
