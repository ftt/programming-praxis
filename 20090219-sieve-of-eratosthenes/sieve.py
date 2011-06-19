#!/usr/bin/env python


import itertools
import sys

# note: the 'modulo' version with the same cut-offs uses much less memory in Python
# but is also way slower
def sieve(n):
    # optimization 1: only odd numbers
    primes = range(3, n + 1, 2)
    upper_bound = n ** 0.5
    for base in xrange(len(primes)):
        if not primes[base]:
            continue
        # optimization 3: stop at the square root of n
        if primes[base] >= upper_bound:
            break
        # optimization 2: start with the square
        for i in xrange(base + (base + 1) * primes[base], len(primes), primes[base]):
            primes[i] = None
    primes.insert(0, 2)
    return filter(None, primes)


def main():
    print 'Enter an upper bound for the sieve.'
    n = int(sys.stdin.readline())
    result = sieve(n)
    print 'Number of primes: {0}\n{1}'.format(len(result), result)


if __name__ == '__main__':
    main()
