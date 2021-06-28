import unittest
from collections import namedtuple

from p1791 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'edges expect')
        # example cases
        self.cases_example = [
            self.Case([[1, 2], [2, 3], [4, 2]], 2),
            self.Case([[1, 2], [5, 1], [1, 3], [1, 4]], 1),
        ]

    # findCenter1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'findCenter1: case: {i}'):
                act = self.solution.findCenter1(Case.edges)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
