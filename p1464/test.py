import unittest
from collections import namedtuple

from p1464 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums expect')
        # example cases
        self.cases_example = [
            self.Case(nums=[3, 4, 5, 2], expect=12),
            self.Case(nums=[1, 5, 4, 5], expect=16),
            self.Case(nums=[3, 7], expect=12),
        ]

    # maxProduct1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'maxProduct1: case: {i}'):
                act = self.solution.maxProduct1(Case.nums)
                self.assertEqual(act, Case.expect)

    # maxProduct2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'maxProduct2: case: {i}'):
                act = self.solution.maxProduct2(Case.nums)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
