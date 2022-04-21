from problem.utils import distancia_euclidiana


class EvaluateTSP:

    def __init__(self, problem_instance):
        self.problem_instance = problem_instance

    def __call__(self, solution):
        distancia = 0

        for idCordenada in range(0, len(solution) - 2):
            x1 = self.problem_instance[solution[idCordenada]][0]
            y1 = self.problem_instance[solution[idCordenada]][1]

            x2 = self.problem_instance[solution[idCordenada + 1]][0]
            y2 = self.problem_instance[solution[idCordenada + 1]][1]

            distancia += distancia_euclidiana(x1, y1, x2, y2)

        total = 100000 - distancia

        if total > 100000 - 800:
            total *= 2.6

        elif total > 100000 - 1000:
            total *= 2.1

        elif total > 100000 - 1500:
            total *= 1.7

        elif total > 100000 - 2500:
            total *= 1.4

        elif total > 100000 - 4000:
            total *= 1.2

        elif total > 100000 - 7000:
            total *= 1.1

        return total
