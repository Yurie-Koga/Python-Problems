import unittest
from collections import namedtuple

from p1281 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'n expect')
        # example cases
        self.cases_example = [
            self.Case(n=234, expect=15),
            self.Case(n=4421, expect=21),
        ]

    # subtractProductAndSum1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'subtractProductAndSum1: case: {i}'):
                act = self.solution.subtractProductAndSum1(Case.n)
                self.assertEqual(act, Case.expect)

    # subtractProductAndSum3
    def test_examples3(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'subtractProductAndSum3: case: {i}'):
                act = self.solution.subtractProductAndSum3(Case.n)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
