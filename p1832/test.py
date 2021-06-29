import unittest
from collections import namedtuple

from p1832 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'sentence expect')
        # example cases
        self.cases_example = [
            self.Case(sentence="thequickbrownfoxjumpsoverthelazydog", expect=True),
            self.Case(sentence="leetcode", expect=False),
        ]

    # checkIfPangram1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'checkIfPangram1: case: {i}'):
                act = self.solution.checkIfPangram1(Case.sentence)
    #             self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
