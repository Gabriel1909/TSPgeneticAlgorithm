from genetic.genetic_algorithm import genetic_algorithm
from genetic.init_population import init_population
from problem.EvaluateTSP import EvaluateTSP
from problem.utils import read_file

if __name__ == '__main__':

    file = read_file('./problem/assets/st70.tsp.txt')
    number = 6000
    max_fitness = 1700

    fn_fitness = EvaluateTSP(file, number)

    population_size = 20
    possible_values = list(file.keys())

    population = init_population(population_size, possible_values)

    solution = genetic_algorithm(population, fn_fitness, fn_thres=max_fitness, ngen=50, pmut=0.3)

    print('Resulting solution: %s' % solution)
    print('Value of resulting solution: %d' % (number - fn_fitness(solution)))
