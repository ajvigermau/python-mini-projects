import copy
import random


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for colours, balls in kwargs.items():
            for i in range(balls):
                self.contents.append(colours)

    def draw(self, balls):
        if balls > len(self.contents):
            removed = self.contents.copy()
            self.contents = []
        else:
            removed = []
            for i in range(balls):
                returned_ball = self.contents.pop(
                    random.randint(0, len(self.contents)-1))
                removed.append(returned_ball)
        return removed


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    N = num_experiments
    M = 0

    for i in range(num_experiments):
        copy_hat = copy.deepcopy(hat)
        extract = copy_hat.draw(num_balls_drawn)

        success = 0
        for colour in expected_balls.keys():
            if extract.count(colour) >= expected_balls[colour]:
                success += 1
        if success == len(expected_balls):
            M += 1
    return M/N


# Example
hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={'red': 2, 'green': 1},
                         num_balls_drawn=5,
                         num_experiments=5)
print(probability)
