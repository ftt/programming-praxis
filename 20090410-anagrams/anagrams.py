import unittest
from operator import mul


def hash_sort(word):
    return "".join(sorted(word))


primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
ord_a = ord("a")


def hash_primes(word):
    # not the same as hash_sort
    return reduce(mul, (primes[ord(c)-ord_a] for c in word if "a" <= c <= "z"), 1)


def build_table(word_list, hash_function):
    table, max_anagrams, largest_class = {}, 0, None
    for word in word_list:
        h = hash_function(word)
        if h not in table:
            table[h] = []
        table[h].append(word)
        # largest anagram class
        if len(table[h]) > max_anagrams:
            max_anagrams, largest_class = len(table[h]), table[h]
    return table, largest_class


def read_words(file_name):
    # each line contains a new-line, so check length + 1
    return [line.strip().lower() for line in open(file_name) if len(line) > 2]


class AnagramTest(unittest.TestCase):
    def test_hash_sort(self):
        words = read_words("/usr/share/dict/words")
        anagram_table, largest_class = build_table(words, hash_sort)
        print largest_class
        self.assertListEqual(anagram_table[hash_sort("stop")], anagram_table[hash_sort("post")])

    def test_hash_primes(self):
        words = read_words("/usr/share/dict/words")
        anagram_table, largest_class = build_table(words, hash_primes)
        print largest_class
        self.assertListEqual(anagram_table[hash_primes("stop")], anagram_table[hash_primes("post")])


if __name__ == "__main__":
    unittest.main()
