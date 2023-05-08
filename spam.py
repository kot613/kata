from itertools import permutations
from operator import mul
import re


def alphametics(puzzle):
    answer = []

    def solve(puzz):
        words = re.findall(r"\w+", puzz)[::-1]
        d = {w[0]: 0 for w in words}
        knz = len(d)
        d.update({c: 0 for c in filter(str.isalpha, puzz)})
        for i, w in enumerate(words):
            for j, c in enumerate(w[::-1]):
                d[c] = d[c] + 10**j * (bool(i) * 2 - 1)
        factors = d.values()
        for p in permutations(range(10), len(d)):
            if 0 in p[:knz]:
                continue
            if not sum(map(mul, factors, p)):
                return dict(zip(d.keys(), p))

    dct = solve(puzzle)
    for el in puzzle:
        answer.append(str(dct.get(el, el)))
    return ''.join(answer)






a = "SATURN + URANUS + NEPTUNE + PLUTO = PLANETS"
print(alphametics(a))


