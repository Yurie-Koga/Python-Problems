import unittest
from collections import namedtuple

from p1732 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'gain expect')
        # example cases
        self.cases_example = [
            self.Case(gain=[-5, 1, 5, 0, -7], expect=1),
            self.Case(gain=[-4, -3, -2, -1, 4, 3, 2], expect=0),
        ]

    # largestAltitude1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'largestAltitude1: case: {i}'):
                act = self.solution.largestAltitude1(Case.gain)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
