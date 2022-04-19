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

        return 100000 - distancia


def distancia_euclidiana(x1, y1, x2, y2):
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
