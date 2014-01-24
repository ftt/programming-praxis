import unittest


_from_roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
_to_roman = {v: k for k, v in _from_roman.items()}


def decode(roman):
    operands = [_from_roman[r] for r in roman]
    total = operands[0]
    for i in xrange(1, len(operands)):
        if operands[i-1] < operands[i]:
            total += operands[i] - 2 * operands[i-1]
        else:
            total += operands[i]
    return total


def encode(number):
    sorted_num_keys = sorted(_to_roman.keys(), reverse=True)
    roman, repetitions = [], 0
    while number > 0:
        for d in sorted_num_keys:
            if number >= d:
                number -= d
                if len(roman) > 0 and _to_roman[d] == roman[-1]:
                    repetitions += 1
                else:
                    repetitions = 0
                roman.append(_to_roman[d])
                break
        # don't bother with multiple Ms, they cannot be compressed
        if repetitions == 3 and roman[-1] != "M":
            # look at Y in YX(*3) and check that it neighbors our X in the key list
            i = _from_roman[roman[-1]]
            if len(roman) > 4 or _from_roman[roman[-5]] - i * 4 == i:
                index = sorted_num_keys.index(_from_roman[roman[-5]]) - 1
            else:
                index = sorted_num_keys.index(_from_roman[roman[-1]]) - 1
            roman = roman[:-5] + [roman[-1], _to_roman[sorted_num_keys[index]]]
    return "".join(roman)


def add_roman_numerals(r1, r2):
    return encode(decode(r1.upper()) + decode(r2.upper()))


class TestRomanNumerals(unittest.TestCase):

    def test_roman_numerals(self):
        self.assertEquals(decode("MDCCXXXII"), 1732)
        self.assertEquals(decode("MDCCCCLVI"), 1956)
        self.assertEquals(decode("MCMLVI"), 1956)
        self.assertEquals(decode("CMLVI"), 956)
        self.assertEquals(encode(1956), "MCMLVI")
        self.assertEquals(add_roman_numerals("CCCLXIX", "CDXLVIII"), "DCCCXVII")


if __name__ == '__main__':
    unittest.main()
