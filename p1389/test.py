import unittest
from collections import namedtuple

from p1389 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums index expect')
        # example cases
        self.cases_example = [
            self.Case(nums=[0, 1, 2, 3, 4], index=[0, 1, 2, 2, 1], expect=[0, 4, 1, 3, 2]),
            self.Case(nums=[1, 2, 3, 4, 0], index=[0, 1, 2, 3, 0], expect=[0, 1, 2, 3, 4]),
            self.Case(nums=[1], index=[0], expect=[1]),
        ]

    # createTargetArray1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'createTargetArray1: case: {i}'):
                act = self.solution.createTargetArray1(Case.nums, Case.index)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
