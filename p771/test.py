import unittest
from collections import namedtuple

from p771 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'jewels stones expect')
        # example cases
        self.cases_example = [
            self.Case(jewels="aA", stones="aAAbbbb", expect=3),
            self.Case(jewels="z", stones="ZZ", expect=0),
            self.Case(jewels="ace", stones="dadc", expect=2),
        ]

    # numJewelsInStones1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'numJewelsInStones1: case: {i}'):
                act = self.solution.numJewelsInStones1(Case.jewels, Case.stones)
                self.assertEqual(act, Case.expect)

    # numJewelsInStones2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'numJewelsInStones2: case: {i}'):
                act = self.solution.numJewelsInStones2(Case.jewels, Case.stones)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
