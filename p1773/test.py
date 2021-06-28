import unittest
from collections import namedtuple

from p1773 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'items ruleKey ruleValue expect')
        # example cases
        self.cases_example = [
            self.Case(
                items=[["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]],
                ruleKey="color",
                ruleValue="silver",
                expect=1
            ),
            self.Case(
                items=[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]],
                ruleKey="type",
                ruleValue="phone",
                expect=2
            ),
        ]

    # countMatches1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'countMatches1: case: {i}'):
                act = self.solution.countMatches1(Case.items, Case.ruleKey, Case.ruleValue)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
