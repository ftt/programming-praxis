# Obviously, import csv


import unittest


def parse_csv(text, sep=",", term="\n"):
    assert(term in ["\n", "\r", "\r\n", "\n\r"])
    assert(len(sep) == 1)
    assert(sep != '"')

    def unquoted_field(field, text):
        eof, eol = text.find(sep), text.find(term)
        if eof != -1 and (eof < eol or eol == -1):
            end, skip, done = eof, len(sep), False
        elif eol != -1:
            end, skip, done = eol, len(term), True
        else:
            end, skip, done = len(text), 0, True
        return field + text[:end], text[end+skip:], done

    def quoted_subfield(text):
        q = text.find('"')
        if q == -1:
            # should this be a parse error?
            return text, ""
        elif q == len(text)-1 or text[q+1] != '"':
            return text[:q], text[q+1:]
        else:
            field = text[:q+1]
            rest_of_field, text = quoted_subfield(text[q+2:])
            return field + rest_of_field, text

    rows, row = [], []
    while len(text) > 0:
        if text[0] != '"':
            field, text, eol = unquoted_field("", text)
        else:
            field, text = quoted_subfield(text[1:])
            field, text, eol = unquoted_field(field, text)
        row.append(field)
        if eol:
            rows.append(row)
            row = []
    return rows


class CsvTester(unittest.TestCase):
    def test_parse_csv(self):
        # I know, I know
        rows = parse_csv(CsvTester.PileOfText)
        self.assertEquals(len(rows), 16)
        self.assertEquals(rows[0], ['1', 'abc', 'def ghi', 'jkl', 'unquoted character strings'])
        self.assertEquals(rows[1], ['2', 'abc', 'def ghi', 'jkl', 'quoted character strings'])
        self.assertEquals(rows[2], ['3', '123', '456', '789', 'numbers'])
        self.assertEquals(rows[3], ['4', ' abc', 'def ', ' ghi ', 'strings with whitespace'])
        self.assertEquals(rows[4], ['5', ' "abc"', 'def ', ' "ghi" ', 'quoted strings with whitespace'])
        self.assertEquals(rows[5], ['6', ' 123', '456 ', ' 789 ', 'numbers with whitespace'])
        self.assertEquals(rows[6], ['7', '\t123', '456\t', '\t789\t', 'numbers with tabs for whitespace'])
        self.assertEquals(rows[7], ['8', ' -123', ' +456', ' 1E3', 'more numbers with whitespace'])
        self.assertEquals(rows[8], ['9', '123 456', '123"456', ' 123 456 ', 'strange numbers'])
        self.assertEquals(rows[9], ['10', 'abc"', 'de"f', 'g"hi', 'embedded quotes'])
        self.assertEquals(rows[10], ['11', 'abc"', 'de"f', 'g"hi', 'quoted embedded quotes'])
        self.assertEquals(rows[11], ['12', '', ' ""', 'x""', 'doubled quotes'])
        self.assertEquals(rows[12], ['13', 'abcdef', 'abc"def"', 'abc "def"', 'strange quotes'])
        self.assertEquals(rows[13], ['14', '', '', ' ', 'empty fields'])
        self.assertEquals(rows[14], ['15', 'abc', 'def\n  ghi', 'jkl', 'embedded newline'])
        self.assertEquals(rows[15], ['16', 'abc', 'def', '789', 'multiple types of fields'])


if __name__ == '__main__':
    with open("csv_file") as f:
        CsvTester.PileOfText = f.read()
    unittest.main()
