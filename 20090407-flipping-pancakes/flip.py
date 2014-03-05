import unittest
from operator import itemgetter


def flipsort(pancakes):
    # divides unsorted and sorted parts
    sorted_mark = len(pancakes)
    while sorted_mark > 0:
        i, m = max(enumerate(pancakes[:sorted_mark]), key=itemgetter(1))
        # if the largest pancake is not in place
        if i < sorted_mark - 1:
            # flip it to the top
            pancakes[:i+1] = reversed(pancakes[:i+1])
            # flip all unsorted pancakes, so that the largest is at the bottom
            pancakes[:sorted_mark] = reversed(pancakes[:sorted_mark])
        sorted_mark -= 1
    return pancakes


class FlipTest(unittest.TestCase):
    def test_flipsort(self):
        self.assertEquals(flipsort([7, 2, 9, 4, 6, 1, 3, 8, 5]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEquals(flipsort([1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 2, 3, 4, 5, 6, 7, 8, 9])
        self.assertEquals(flipsort([9, 8, 7, 6, 5, 4, 3, 2, 1]), [1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
