"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""

from random import randint, choice
from my_solution import count_chains


def make_random_tests(num):
    random_tests = []
    for _ in range(num):
        circles = []
        for _ in range(randint(1, 10)):
            r = choice([1, 1, 1, 2, 2, 2, 3, 3, 4])
            x = randint(-10, 10)
            y = randint(-10, 10)
            if (x, y, r) not in circles:
                circles.append((x, y, r))
        random_tests.append({'input': circles,
                             'answer': count_chains(circles)})
    return random_tests


TESTS = {
    "Basics": [
        {
            "input": [[1, 1, 1], [4, 2, 1], [4, 3, 1]],
            "answer": 2,
            "explanation": 'basic'
        },
        {
            "input": [[1, 1, 1], [2, 2, 1], [3, 3, 1]],
            "answer": 1,
            "explanation": 'basic #2'
        },
        {
            "input": [[2, 2, 2], [4, 2, 2], [3, 4, 2]],
            "answer": 1,
            "explanation": 'trinity'
        },
        {
            "input": [[2, 2, 1], [2, 2, 2]],
            "answer": 2,
            "explanation": 'Inclusion'
        },
        {
            "input": [[1, 1, 1], [1, 3, 1], [3, 1, 1], [3, 3, 1]],
            "answer": 4,
            "explanation": 'adjacent'
        },
        {
            "input": [[0, 0, 1], [-1, 1, 1], [1, -1, 1], [-2, -2, 1]],
            "answer": 2,
            "explanation": 'negative coordinates'
        },
        {
            "input": [[1, 3, 1], [2, 2, 1], [4, 2, 1], [5, 3, 1], [3, 3, 1]],
            "answer": 1,
        },
        {
            "input": [[1, 1, 1], [0, 2, 1], [1, 3, 1], [2, 2, 1]],
            "answer": 1,
        },
        {
            "input": [[0, 0, 2], [1, 0, 3], [3, 0, 1], [2, 1, 1], [-2, -2, 1], [0, 0, 4], [-3, 0, 1]],
            "answer": 3,
        },
    ],
    'Randoms': make_random_tests(10),
}
