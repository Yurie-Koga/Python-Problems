import unittest
from collections import namedtuple

from p1480 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums expect')
        # example cases
        self.cases_example = [
            self.Case([1, 2, 3, 4], [1, 3, 6, 10]),
            self.Case([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
            self.Case([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
        ]

    # runningSum1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'runningSum1: case: {i}'):
                act = self.solution.runningSum1(Case.nums)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
