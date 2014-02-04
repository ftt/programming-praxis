# From http://collaboration.cmc.ec.gc.ca/science/rpn/biblio/ddj/Website/articles/DDJ/1995/9504/9504k/9504k.htm
# Don't bother with Julian calendars because it was accepted inconsistently and is not relevant to the task


import unittest


def weekday(day, month, year):
    # Monday = 0, ..., Sunday = 6
    if month < 3:
        month += 12
        year -= 1
    return (day + 2 * month + 3 * (month + 1) / 5 + year + year / 4 - year / 100 + year / 400) % 7


def count_fridays_13(year, month):
    count = 0
    for m in xrange(month, 13):
        # Friday is 4
        if weekday(13, m, year) == 4:
            count += 1
    return count


class FridayTester(unittest.TestCase):
    def test_gauss_weekday(self):
        self.assertEqual(weekday(1, 1, 1983), 5)
        self.assertEqual(weekday(1, 2, 1983), 1)
        self.assertEqual(weekday(1, 3, 1983), 1)
        self.assertEqual(weekday(1, 4, 1983), 4)
        self.assertEqual(weekday(17, 10, 1983), 0)

    def test_count_fridays_13(self):
        self.assertEqual(count_fridays_13(1983, 1), 1)
        self.assertEqual(count_fridays_13(2009, 1), 3)

    def test_task(self):
        count = count_fridays_13(2009, 4)
        for y in xrange(2010, 2019):
            count += count_fridays_13(y, 1)
        self.assertEqual(count, 17)


if __name__ == '__main__':
    unittest.main()
