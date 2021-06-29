import unittest
from collections import namedtuple

from p1844 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 's expect')
        # example cases
        self.cases_example = [
            self.Case(s="a1c1e1", expect="abcdef"),
            self.Case(s="a1b2c3d4e", expect="abbdcfdhe"),
        ]

    # replaceDigits1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'replaceDigits1: case: {i}'):
                act = self.solution.replaceDigits1(Case.s)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
