import unittest
from collections import namedtuple

from p import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'nums expect')
        # example cases
        self.cases_example = [
            # self.Case(, expect=),
        ]

    # twoSum1
    # def test_examples1(self):
    #     for i, Case in enumerate(self.cases_example):
    #         with self.subTest(f'twoSum1: case: {i}'):
    #             act = self.solution.print_text(Case.nums)
    #             self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
