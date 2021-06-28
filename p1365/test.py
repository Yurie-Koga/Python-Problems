import unittest
from collections import namedtuple

from p1365 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums expect')
        # example cases
        self.cases_example = [
            self.Case([8, 1, 2, 2, 3], [4, 0, 1, 1, 3]),
            self.Case([6, 5, 4, 8], [2, 1, 0, 3]),
            self.Case([7, 7, 7, 7], [0, 0, 0, 0]),
        ]

    # smallerNumbersThanCurrent1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'smallerNumbersThanCurrent1: case: {i}'):
                act = self.solution.smallerNumbersThanCurrent1(Case.nums)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
