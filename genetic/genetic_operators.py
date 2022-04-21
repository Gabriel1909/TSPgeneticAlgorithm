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
