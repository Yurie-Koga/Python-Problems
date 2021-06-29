import unittest
from collections import namedtuple

from p1342 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'num expect')
        # example cases
        self.cases_example = [
            self.Case(num=14, expect=6),
            self.Case(num=8, expect=4),
            self.Case(num=123, expect=12),
        ]

    # numberOfSteps1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'numberOfSteps1: case: {i}'):
                act = self.solution.numberOfSteps1(Case.num)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
