import unittest


def josephus(people, turn):
    circle = range(people)
    executed = []
    step, current = turn - 1, 0
    while len(circle) > 1:
        current = (current + step) % len(circle)
        executed.append(circle.pop(current))
    return executed + circle


class TestSudoku(unittest.TestCase):

    def test_josephus(self):
        self.assertEqual(josephus(41, 3), [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35, 38, 0, 4, 9, 13, 18, 22, 27, 31, 36, 40, 6, 12, 19, 25, 33, 39, 7, 16, 28, 37, 10, 24, 1, 21, 3, 34, 15, 30])
        self.assertEqual(josephus(0, 3), [])


if __name__ == '__main__':
    unittest.main()
