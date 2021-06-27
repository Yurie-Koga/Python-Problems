import unittest
from collections import namedtuple

from p import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums target expect')
        # example cases
        self.cases_example = [
            self.Case([2, 7, 11, 15], 9, [0, 1]),
            self.Case([3, 2, 4], 6, [1, 2]),
            self.Case([3, 3], 6, [0, 1]),
        ]

    # twoSum1
    # def test_examples1(self):
    #     for i, Case in enumerate(self.cases_example):
    #         with self.subTest(f'twoSum1: case: {i}'):
    #             act = self.solution.print_text(Case.nums, Case.target)
    #             self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
