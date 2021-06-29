import unittest
from collections import namedtuple

from p1672 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'accounts expect')
        # example cases
        self.cases_example = [
            self.Case([[1, 2, 3], [3, 2, 1]], 6),
            self.Case([[1, 5], [7, 3], [3, 5]], 10),
            self.Case([[2, 8, 7], [7, 1, 3], [1, 9, 5]], 17),
        ]

    # maximumWealth1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'maximumWealth1: case: {i}'):
                act = self.solution.maximumWealth1(Case.accounts)
                self.assertEqual(act, Case.expect)

    # maximumWealth2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'maximumWealth2: case: {i}'):
                act = self.solution.maximumWealth2(Case.accounts)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
