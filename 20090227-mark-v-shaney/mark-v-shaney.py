import collections
import random
import sys


class TrigramModel(object):
    def __init__(self):
        """ Initializes model data structures:
        pair_extensions -- a dictionary with pairs of tokens as keys and Counter dictionaries of possible continuations
        tokens -- list of all tokens
        """
        self.pair_extensions = collections.defaultdict(lambda: collections.Counter())
        self.tokens = []

    def train(self, token_list):
        for i in xrange(len(token_list)):
            if i > 1:
                self.pair_extensions[(token_list[i-2], token_list[i-1])][token_list[i]] += 1

    def extend_pair(self, starting_pair=None):
        """Takes a pair of tokens or None to extend."""
        # choose an element based on its weight
        def choose(collection, scorer, tester=lambda smth: True):
            scores = dict.fromkeys((e for e in collection if tester(e)), 0)
            min_score = float("inf")
            for k in scores:
                scores[k] = scorer(k)
                if scores[k] < min_score:
                    min_score = scores[k]
            min_score -= 1
            rnd = random.random() * (sum(scores.values()) + len(scores) * abs(min_score))
            for k in scores:
                rnd -= scores[k] + abs(min_score)
                if rnd < 0:
                    return k

        # choose a staring pair
        if starting_pair is None:
            return choose(self.pair_extensions, scorer=lambda p: sum(self.pair_extensions[p].values()), tester=lambda p: p[0].istitle())
        elif len(starting_pair) == 2:
            return choose(self.pair_extensions[starting_pair].keys(), scorer=lambda t: self.pair_extensions[starting_pair][t])
        else:
            raise ValueError("starting_pair")


def process_corpus(file_name, model):
    with open(file_name) as f:
        model.train(f.read().split())
    pair = model.extend_pair()
    text = list(pair)
    while not text[-1].endswith((".", "?", "!")) or len(text) < 30:
        text.append(model.extend_pair(pair))
        pair = tuple(text[-2:])
    return " ".join(text)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Need a plain text corpus."
    else:
        model = TrigramModel()
        print process_corpus(sys.argv[1], model)
