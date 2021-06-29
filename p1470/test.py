import unittest
from collections import namedtuple

from p1470 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums n expect')
        # example cases
        self.cases_example = [
            self.Case(nums=[1, 3, 2, 4], n=2, expect=[1, 2, 3, 4]),
            self.Case(nums=[2, 5, 1, 3, 4, 7], n=3, expect=[2, 3, 5, 4, 1, 7]),
            self.Case(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4, expect=[1, 4, 2, 3, 3, 2, 4, 1]),
            self.Case(nums=[1, 1, 2, 2], n=2, expect=[1, 2, 1, 2]),
        ]

    # shuffle1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'shuffle1: case: {i}'):
                act = self.solution.shuffle1(Case.nums, Case.n)
                self.assertEqual(act, Case.expect)

    # shuffle2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'shuffle2: case: {i}'):
                act = self.solution.shuffle2(Case.nums, Case.n)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
