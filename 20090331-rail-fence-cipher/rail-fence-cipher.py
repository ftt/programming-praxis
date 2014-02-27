import unittest
from itertools import izip_longest as pair


def permutate(sequence, key):
    permutated, period = [], key * 2 - 2
    for level in xrange(key):
        first = sequence[level::period]
        shift = period - 2 * level
        if shift in [0, period]:
            second = []
        else:
            second = sequence[level+shift::period]
        # join both halves into pairs with None as a filler,
        # then unroll all tuples into a single list,
        # then leave out Nones
        permutated.extend(filter(lambda x: x is not None, (c for tup in pair(first, second) for c in tup)))
    return permutated


def encrypt(text, key):
    return "".join(permutate(text, key))


def decrypt(cipher, key):
    indices = permutate(range(len(cipher)), key)
    # pair "encrypted" indices with cipher characters,
    # then sort them into proper order
    return "".join(tup[1] for tup in sorted(zip(indices, cipher)))


class CipherTest(unittest.TestCase):
    def test_encrypt(self):
        self.assertEquals(encrypt("PROGRAMMING PRAXIS", 4), "PMPRAM RSORIGAIGNX")
        self.assertEquals(encrypt("PROGRAMMING PRAXIS", 5), "PIIRMNXSOMGAGA RRP")

    def test_decrypt(self):
        self.assertEquals(decrypt("PMPRAM RSORIGAIGNX", 4), "PROGRAMMING PRAXIS")
        self.assertEquals(decrypt("PIIRMNXSOMGAGA RRP", 5), "PROGRAMMING PRAXIS")


if __name__ == "__main__":
    unittest.main()
