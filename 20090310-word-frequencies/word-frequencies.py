import sys


# generally, Counter from the standard library would be more appropriate
def count_words(filename, n):
    counts = {}
    with open(filename) as f:
        line = f.readline()
        # defaultdict here
        while line != "":
            words = (w.strip() for w in line.split())
            for w in words:
                c = counts.get(w, 0)
                counts[w] = c + 1
            line = f.readline()
    # bisect here, or just sort the dictionary by counts
    champions, min_count = [], 0
    for word, count in counts.iteritems():
        if count > min_count:
            i = 0
            for i, pair in enumerate(champions):
                if pair[1] < count:
                    break
            champions[i:i] = [(word, count)]
            if len(champions) > n:
                champions = champions[:n]
            min_count = champions[-1][1]
    return champions


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print "Usage: {0} <filename> <n>.".format(sys.argv[0])
    else:
        for result in count_words(sys.argv[1], int(sys.argv[2])):
            print "{0}\t{1}".format(*result)
