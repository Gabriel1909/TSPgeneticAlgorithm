import pandas as pd

from genetic.genetic_algorithm import genetic_algorithm
from genetic.init_population import init_population
from problem.EvaluateTSP import EvaluateTSP

if __name__ == '__main__':

    ds = pd.read_csv('./problem/assets/st70.tsp.txt', header=None)

    arquivo = dict()

    for row in ds.itertuples():
        linha = row[1].split()

        arquivo[int(linha[0]) - 1] = [int(linha[1]), int(linha[2])]

    fn_fitness = EvaluateTSP(arquivo)

    population_size = 10
    possible_values = list(arquivo.keys())

    individual_length = len(arquivo)

    population = init_population(population_size, possible_values, individual_length)

    solution = genetic_algorithm(population, fn_fitness, gene_pool=possible_values, fn_thres=100000-675, ngen=1000)

    print('Resulting solution: %s' % solution)
    print('Value of resulting solution: %d' % (100000 - fn_fitness(solution)))

    repeats = set([item for item in solution if solution.count(item) > 1])
    print(repeats)
