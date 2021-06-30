import unittest
from collections import namedtuple

from p1704 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 's expect')
        # example cases
        self.cases_example = [
            self.Case(s="book", expect=True),
            self.Case(s="textbook", expect=False),
            self.Case(s="MerryChristmas", expect=False),
            self.Case(s="AbCdEfGh", expect=True),
            self.Case(s="Uo", expect=True),
        ]

    # halvesAreAlike1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'halvesAreAlike1: case: {i}'):
                act = self.solution.halvesAreAlike1(Case.s)
                self.assertEqual(act, Case.expect)

    # halvesAreAlike2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'halvesAreAlike2: case: {i}'):
                act = self.solution.halvesAreAlike2(Case.s)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
