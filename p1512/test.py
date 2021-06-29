import unittest
from collections import namedtuple

from p1512 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums expect')
        # example cases
        self.cases_example = [
            self.Case(nums=[1, 2, 3, 1, 1, 3], expect=4),
            self.Case(nums=[1, 1, 1, 1], expect=6),
            self.Case(nums=[1, 2, 3], expect=0),
        ]

    # numIdenticalPairs1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'numIdenticalPairs1: case: {i}'):
                act = self.solution.numIdenticalPairs1(Case.nums)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
