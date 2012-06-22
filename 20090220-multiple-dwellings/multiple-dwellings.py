import itertools


floors = range(5)
b, c, f, m, s = range(5)
fletcher_range = range(1, 4)

def valid(arrangement):
    return (arrangement[b] != 4 and
            arrangement[c] != 0 and
            arrangement[f] in fletcher_range and
            arrangement[m] > arrangement[c] and
            abs(arrangement[s] - arrangement[f]) > 1 and
            abs(arrangement[c] - arrangement[f]) > 1)

assert filter(valid, itertools.permutations(floors)) == [(2, 1, 3, 4, 0)]
