import unittest


def bsearch(needle, haystack):
    def search(start, end):
        if start >= end:
            return -1
        middle = (start + end) / 2
        if needle == haystack[middle]:
            return middle
        elif needle < haystack[middle]:
            return search(start, middle)
        else:
            return search(middle + 1, end)
    return search(0, len(haystack))


class NotFound(Exception):
    pass


def bsearch_slice(needle, haystack):
    def search(truss):
        if len(truss) == 0:
            raise NotFound()
        middle = len(truss) / 2
        if needle == truss[middle]:
            return middle
        elif needle < truss[middle]:
            return search(truss[:middle])
        else:
            return middle + 1 + search(truss[middle+1:])
    try:
        return search(haystack)
    except NotFound:
        return -1


class BinarySearchTest(unittest.TestCase):
    def test_search(self):
        self.assertEquals(bsearch(19, [13, 19, 24, 29, 32, 37, 43]), 1)
        self.assertEquals(bsearch(32, [13, 19, 24, 29, 32, 37, 43]), 4)
        self.assertEquals(bsearch(33, [13, 19, 24, 29, 32, 37, 43]), -1)
        self.assertEquals(bsearch(32, [32, 32, 32]), 1)

    def test_search_slice(self):
        self.assertEquals(bsearch_slice(19, [13, 19, 24, 29, 32, 37, 43]), 1)
        self.assertEquals(bsearch_slice(32, [13, 19, 24, 29, 32, 37, 43]), 4)
        self.assertEquals(bsearch_slice(33, [13, 19, 24, 29, 32, 37, 43]), -1)
        self.assertEquals(bsearch_slice(32, [32, 32, 32]), 1)


if __name__ == '__main__':
    unittest.main()
