import unittest
from collections import namedtuple

from p1859 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 's expect')
        # example cases
        self.cases_example = [
            self.Case(s="is2 sentence4 This1 a3", expect="This is a sentence"),
            self.Case(s="Myself2 Me1 I4 and3", expect="Me Myself and I"),
        ]

    # sortSentence1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'sortSentence1: case: {i}'):
                act = self.solution.sortSentence1(Case.s)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
