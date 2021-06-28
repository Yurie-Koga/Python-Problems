import unittest
from collections import namedtuple

from p1486 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'n start expect')
        # example cases
        self.cases_example = [
            self.Case(5, 0, 8),
            self.Case(4, 3, 8),
            self.Case(1, 7, 7),
            self.Case(10, 5, 2),
        ]

    # xorOperation1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'twoSum1: case: {i}'):
                act = self.solution.xorOperation1(Case.n, Case.start)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
