from problem.utils import euclidean_distance


class EvaluateTSP:

    def __init__(self, problem_instance, number):
        self.problem_instance = problem_instance
        self.number = number

    def __call__(self, solution):
        distance = 0

        for cordinate_id in range(0, len(solution) - 2):
            distance += self.calculate_distance(cordinate_id, cordinate_id + 1, solution)

        distance += self.calculate_distance(0, -1, solution)

        return self.number - distance

    def calculate_distance(self, coordinate_x, coordinate_y, solution):
        x1, y1 = self.get_coordinates(coordinate_x, solution)

        x2, y2 = self.get_coordinates(coordinate_y, solution)
        return euclidean_distance(x1, y1, x2, y2)

    def get_coordinates(self, coordinate, solution):
        return self.problem_instance[solution[coordinate]][0], \
               self.problem_instance[solution[coordinate]][1]
