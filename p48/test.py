import unittest
from collections import namedtuple

from p48 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'matrix expect')
        # example cases
        self.cases_example = [
            self.Case([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 4, 1], [8, 5, 2], [9, 6, 3]]),
            self.Case([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]],
                      [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]),
            self.Case([[1]], [[1]]),
            self.Case([[1, 2], [3, 4]], [[3, 1], [4, 2]]),
            # self.Case([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[7, 2, 1], [4, 5, 6], [9, 8, 3]]),  # moved corner
            # self.Case([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], [[13, 2, 3, 1], [5, 6, 7, 8], [9, 10, 11, 12], [16, 14, 15, 4]])
        ]

    # rotate1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'rotate1: case: {i}'):
                act = self.solution.rotate1(Case.matrix)
                self.assertEqual(act, Case.expect)

    # rotate2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'rotate2: case: {i}'):
                act = self.solution.rotate2(Case.matrix)
                self.assertEqual(act, Case.expect)

if __name__ == '__main__':
    unittest.main()
