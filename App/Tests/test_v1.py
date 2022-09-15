import csv, sys, unittest as ut

sys.path.insert(0, '../Logic')
from Queens import get_queens

def get_solution(n: int):
    if (n < 1): return

    solution = None

    with open('./solutions.csv', mode= 'r') as solutions:
        reader = csv.reader(solutions, delimiter= ',')

        solution = list(reader)[n][2]

    return int(solution)

class TestQueens(ut.TestCase):
    def test_lows(self):
        for n in range(1,9):
            solution = get_solution(n)

            self.assertEqual(len(get_queens(n)), solution)

    def test_high(self):
        solution = get_solution(11)
        self.assertEqual(len(get_queens(11)), solution)

if __name__ == "__main__":
    ut.main()
