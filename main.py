from genetic.genetic_algorithm import genetic_algorithm
from genetic.init_population import init_population
from problem.EvaluateTSP import EvaluateTSP
from problem.utils import ler_arquivo

if __name__ == '__main__':
    arquivo = ler_arquivo()

    fn_fitness = EvaluateTSP(arquivo)

    population_size = 30
    possible_values = list(arquivo.keys())

    population = init_population(population_size, possible_values)

    solution = genetic_algorithm(population, fn_fitness, fn_thres=6000 - 675, ngen=1000)

    print('Resulting solution: %s' % solution)
    print('Value of resulting solution: %d' % (6000 - fn_fitness(solution)))

    repeats = set([item for item in solution if solution.count(item) > 1])
    print(repeats)
