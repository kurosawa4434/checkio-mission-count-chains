from math import hypot
from collections import defaultdict


def count_chains(circles):

    rest = list(circles)

    colors = defaultdict(int)
    rest = set(circles)

    def set_color(circle, c):
        stack = [circle]
        while stack:
            tx, ty, tr = stack.pop()
            for r in list(rest):
                rx, ry, rr = r
                if abs(tr-rr) < hypot(tx-rx, ty-ry) < tr+rr:
                    colors[r] = c
                    stack.append(r)
                    rest.remove(r)

    c = 0
    for circle in circles:
        if not colors[circle]:
            c += 1
            colors[circle] = c
            set_color(circle, c)

    return c


if __name__ == '__main__':
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")
