import unittest
from collections import namedtuple

from p1021 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 's expect')
        # example cases
        self.cases_example = [
            self.Case(s="(()())(())", expect="()()()"),
            self.Case(s="(()())(())(()(()))", expect="()()()()(())"),
            self.Case(s="()()", expect=""),
        ]

    # removeOuterParentheses1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'removeOuterParentheses1: case: {i}'):
                act = self.solution.removeOuterParentheses1(Case.s)
                self.assertEqual(act, Case.expect)

    # removeOuterParentheses2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'removeOuterParentheses2: case: {i}'):
                act = self.solution.removeOuterParentheses2(Case.s)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
