import unittest
from collections import namedtuple

from p1528 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 's indices expect')
        # example cases
        self.cases_example = [
            self.Case(s="codeleet", indices=[4, 5, 6, 7, 0, 2, 1, 3], expect="leetcode"),
            self.Case(s="abc", indices=[0, 1, 2], expect="abc"),
            self.Case(s="aiohn", indices=[3, 1, 4, 2, 0], expect="nihao"),
            self.Case(s="aaiougrt", indices=[4, 0, 2, 6, 7, 3, 1, 5], expect="arigatou"),
            self.Case(s="art", indices=[1, 0, 2], expect="rat"),
        ]

    # restoreString1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'restoreString1: case: {i}'):
                act = self.solution.restoreString1(Case.s, Case.indices)
                self.assertEqual(act, Case.expect)

    # restoreString2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'restoreString2: case: {i}'):
                act = self.solution.restoreString2(Case.s, Case.indices)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
