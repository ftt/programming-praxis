import unittest


def rot13(input):
    a, A = ord('a'), ord('A')
    n, N = a + 13, A + 13
    m, M = n - 1, N - 1
    z, Z = m + 13, M + 13
    
    def rot_char(c):
        c = ord(c)
        if a <= c <= m or A <= c <= M:
            c += 13
        elif n <= c <= z or N <= c <= Z:
            c -= 13
        return chr(c)
    
    return ''.join(rot_char(c) for c in input)

class TestROT13(unittest.TestCase):

    def test_rot13(self):
        self.assertEqual(rot13(''), '')
        self.assertEqual(rot13('abcdefghijklmnopqrstuvwxyz'), 'nopqrstuvwxyzabcdefghijklm')
        self.assertEqual(rot13('NOPQRSTUVWXYZABCDEFGHIJKLM'), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        self.assertEqual(rot13('Cebtenzzvat Cenkvf vf sha!'), 'Programming Praxis is fun!')
        self.assertEqual(rot13('Programming Praxis is fun!'), 'Cebtenzzvat Cenkvf vf sha!')


if __name__ == '__main__':
    unittest.main()
