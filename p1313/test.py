import unittest
from collections import namedtuple

from p1313 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums expect')
        # example cases
        self.cases_example = [
            self.Case(nums=[1, 2, 3, 4], expect=[2, 4, 4, 4]),
            self.Case(nums=[1, 1, 2, 3], expect=[1, 3, 3])
        ]

    # decompressRLElist1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'decompressRLElist1: case: {i}'):
                act = self.solution.decompressRLElist1(Case.nums)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
