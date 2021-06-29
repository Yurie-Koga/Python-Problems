import unittest
from collections import namedtuple

from p1816 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 's k expect')
        # example cases
        self.cases_example = [
            self.Case(s="Hello how are you Contestant", k=4, expect="Hello how are you"),
            self.Case(s="What is the solution to this problem", k=4, expect="What is the solution"),
            self.Case(s="chopper is not a tanuki", k=5, expect="chopper is not a tanuki"),
        ]

    # truncateSentence1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'truncateSentence1: case: {i}'):
                act = self.solution.truncateSentence1(Case.s, Case.k)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
