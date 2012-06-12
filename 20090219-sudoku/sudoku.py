import copy
import unittest


digits = '123456789'
size = 9
squares = dict.fromkeys([(r, c) for r in xrange(size) for c in xrange(size)])

def create_empty_grid():
    square_centers = ((r, c) for r in xrange(1, size, 3) for c in xrange(1, size, 3))
    square_centers = list(enumerate(square_centers))
    cells = dict.fromkeys([(r, c) for r in xrange(size) for c in xrange(size)])
    for c in cells:
        i, v = min(square_centers, key = lambda sc: sum([abs(c[0] - sc[1][0]), abs(c[1] - sc[1][1])]))
        cells[c] = digits
        squares[c] = i
    return cells

def print_grid(grid):
    if grid is None:
        print 'NONE'
        return
    col_width = max(len(grid[c]) for c in grid)
    for r in xrange(size):
        print ''.join(grid[r, c].center(col_width) + ('|' if c % 3 == 2 else ' ') for c in xrange(size))
        if r % 3 == 2:
            print '-' * (col_width + 1) * 9

def unroll_grid(grid):
    if grid is None:
        return 'NONE'
    return ''.join([grid[(r, c)] for r in xrange(size) for c in xrange(size)])

def affected_cells(grid, cell):
    c0, c1, s = cell[0], cell[1], squares[cell]
    affected = set(c for c in grid if c[0] == c0 or c[1] == c1 or squares[c] == s)
    return affected.difference([cell])

def solve_grid(grid, raw):
    raw_values = [c for c in raw if c in digits or c == '0']
    assert len(raw_values) == size * size
    for r in xrange(size):
        for c in xrange(size):
            i = size * r + c
            if raw_values[i] != '0':
                grid = assign(grid, (r, c), raw_values[i])
                if not grid:
                    raise ValueError('Initial grid is confusing')
    return search(grid)

def eliminate(grid, cell, value):
    if value not in grid[cell]:
        return grid
    peers = affected_cells(grid, cell)
    grid[cell] = grid[cell].replace(value, '')
    if len(grid[cell]) == 0:
        return None
    elif len(grid[cell]) == 1:
        the_value = grid[cell]
        if not all(eliminate(grid, c, the_value) for c in peers):
            return None
    
    return grid

def assign(grid, cell, value):
    free_values = grid[cell].replace(value, '')
    if all(eliminate(grid, cell, v) for v in free_values):
        return grid
    return None

def search(grid):
    if grid is None or all([len(grid[c]) == 1 for c in grid]):
        return grid
    def value_count(cell):
        l = len(grid[cell])
        return l if l > 1 else 10
    next_cell = min(grid, key = value_count)
    for v in grid[next_cell]:
        solution = search(assign(grid.copy(), next_cell, v))
        if solution is not None:
            return solution


class TestSudoku(unittest.TestCase):

    def test_create_empty_grid(self):
        cells = create_empty_grid()
        self.assertEqual(len(cells), size * size)
        self.assertEqual(len(set(c[0] for c in cells)), size)
        self.assertEqual(len(set(c[1] for c in cells)), size)
        self.assertEqual(len(set(squares.values())), size)
        self.assertEqual(squares[(5, 3)], 4)
        self.assertEqual(squares[(0, 0)], 0)
        self.assertEqual(squares[(8, 8)], 8)
        self.assertEqual(squares[(7, 1)], 6)

    def test_affected_cells(self):
        cells = create_empty_grid()
        set0 = set([(0, 3), (1, 3), (2, 3), (3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 0), (5, 1), (5, 2), (5, 4), (5, 5), (5, 6), (5, 7), (5, 8), (6, 3), (7, 3), (8, 3)])
        self.assertEqual(affected_cells(cells, (5, 3)), set0)
        set1 = set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (4, 0), (5, 0), (6, 0), (7, 0), (8, 0)])
        self.assertEqual(affected_cells(cells, (0, 0)), set1)
        set2 = set([(0, 8), (1, 8), (2, 8), (3, 8), (4, 8), (5, 8), (6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2), (8, 3), (8, 4), (8, 5), (8, 6), (8, 7)])
        self.assertEqual(affected_cells(cells, (8, 8)), set2)
        set3 = set([(0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 0), (6, 1), (6, 2), (7, 0), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7), (7, 8), (8, 0), (8, 1), (8, 2)])
        self.assertEqual(affected_cells(cells, (7, 1)), set3)

    def test_solver(self):
        grid = create_empty_grid()
        grid = solve_grid(grid, '700100000020000015000006390200018000040090070000750003078500000560000040000001002')
        self.assertEqual(unroll_grid(grid), '789135624623947815451286397237418569845693271916752483178524936562379148394861752')
        grid = create_empty_grid()
        grid = solve_grid(grid, '700100000020000015000006390200018000040090070000750003078500000560000040003001002')
        self.assertEqual(unroll_grid(grid), 'NONE')


if __name__ == '__main__':
    unittest.main()
