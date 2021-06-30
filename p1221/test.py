import unittest
from collections import namedtuple

from p1221 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 's expect')
        # example cases
        self.cases_example = [
            self.Case(s="RLRRLLRLRL", expect=4),
            self.Case(s="RLLLLRRRLR", expect=3),
            self.Case(s="LLLLRRRR", expect=1),
            self.Case(s="RLRRRLLRLL", expect=2),
        ]

    # balancedStringSplit1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'balancedStringSplit1: case: {i}'):
                act = self.solution.balancedStringSplit1(Case.s)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
