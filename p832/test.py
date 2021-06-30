import unittest
from collections import namedtuple

from p832 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'image expect')
        # example cases
        self.cases_example = [
            self.Case(image=[[1, 1, 0], [1, 0, 1], [0, 0, 0]],
                      expect=[[1, 0, 0], [0, 1, 0], [1, 1, 1]]),
            self.Case(image=[[1, 1, 0, 0], [1, 0, 0, 1], [0, 1, 1, 1], [1, 0, 1, 0]],
                      expect=[[1, 1, 0, 0], [0, 1, 1, 0], [0, 0, 0, 1], [1, 0, 1, 0]]),
        ]

    # flipAndInvertImage1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'flipAndInvertImage1: case: {i}'):
                act = self.solution.flipAndInvertImage1(Case.image)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
