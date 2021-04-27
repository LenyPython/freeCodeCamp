import copy
import random
from random import randint


class Hat:
    def __init__(self, **kwargs):
        self.contents = [color for color,
                         times in kwargs for _ in range(times)]

    def draw(self, number):
        if number > len(self.contents):
            return self.contents

        poped = list()
        for _ in range(number):
            element = self.contents.pop(randint(0, len(self.contents) - 1))
            poped.append(element)
        return poped


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    original = copy.deepcopy(hat.contents)
    for _ in range(num_experiments):
        result = hat.draw(num_balls_drawn)
        if all(expected_balls[key] <= result.count(key) for key in expected_balls):
            count += 1
        hat.contents = copy.deepcopy(original)
    return count / num_experiments
