import unittest
from collections import namedtuple

from p1662 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'word1 word2 expect')
        # example cases
        self.cases_example = [
            self.Case(word1=["ab", "c"], word2=["a", "bc"], expect=True),
            self.Case(word1=["a", "cb"], word2=["ab", "c"], expect=False),
            self.Case(word1=["abc", "d", "defg"], word2=["abcddefg"], expect=True),
        ]

    # arrayStringsAreEqual1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'arrayStringsAreEqual1: case: {i}'):
                act = self.solution.arrayStringsAreEqual1(Case.word1, Case.word2)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
