#!/usr/bin/env python


import random


WIN_INDICES = [
    range(0, 5), # columns
    range(5, 10),
    range(10, 15),
    range(15, 20),
    range(20, 25),
    range(0, 25, 5), # rows
    range(1, 25, 5),
    range(2, 25, 5),
    range(3, 25, 5),
    range(4, 25, 5),
    [0, 6, 12, 18, 24], # diagonals
    [4, 8, 12, 16, 20]
]


def make_card():
    card = []
    # fill by columns
    card.extend(random.sample(xrange(1, 15), 5))
    card.extend(random.sample(xrange(16, 30), 5))
    card.extend(random.sample(xrange(31, 45), 5))
    card.extend(random.sample(xrange(46, 60), 5))
    card.extend(random.sample(xrange(61, 75), 5))
    card[12] = 0
    return card


def check_bingo(card, number):
    for i in xrange(25):
        if card[i] == number:
            card[i] = 0
    for indices in WIN_INDICES:
        if sum(card[i] for i in indices) == 0:
            return True
    return False

def play(cards):
    pool = range(1, 76)
    random.shuffle(pool)
    calls = 0
    while pool:
        number = pool.pop()
        calls += 1
        for c in cards:
            if check_bingo(c, number):
                return calls
    return calls


def main():
    print 'Average number of calls required before a single card achieves bingo: {0}'.format(sum(play([make_card()]) for i in xrange(100)) * 0.01)
    print 'Average number of calls required before any card among five hundred in play achieves bingo: {0}'.format(sum(play([make_card() for j in xrange(500)]) for i in xrange(100)) * 0.01)

if __name__ == '__main__':
    main()
