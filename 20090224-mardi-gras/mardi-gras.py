import datetime
import unittest


def computus(year):
    a = year % 19
    b = year >> 2
    c = b // 25 + 1
    d = (c * 3) >> 2
    e = ((a * 19) - ((c * 8 + 5) // 25) + d + 15) % 30
    e += (29578 - a - e * 32) >> 10
    e -= ((year % 7) + b - d + e + 2) % 7
    d = e >> 5
    day = e - d * 31
    month = d + 3
    return datetime.date(year, month, day)

def mardi_gras(year):
    easter = computus(year)
    return easter + datetime.timedelta(days = -5, weeks = -6)

class TestMardiGras(unittest.TestCase):

    def test_computus(self):
        self.assertEqual(computus(2009), datetime.date(2009, 4, 12))
        self.assertEqual(computus(1989), datetime.date(1989, 3, 26))
        self.assertEqual(computus(2049), datetime.date(2049, 4, 18))
        self.assertEqual(computus(2012), datetime.date(2012, 4, 8))

    def test_mardi_gras(self):
        self.assertEqual(mardi_gras(2009), datetime.date(2009, 2, 24))
        self.assertEqual(mardi_gras(1989), datetime.date(1989, 2, 7))
        self.assertEqual(mardi_gras(2049), datetime.date(2049, 3, 2))
        self.assertEqual(mardi_gras(2012), datetime.date(2012, 2, 21))


if __name__ == '__main__':
    unittest.main()
