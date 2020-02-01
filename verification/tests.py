"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


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
    ]
}
