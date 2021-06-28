import unittest
from collections import namedtuple

from p1108 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'address expect')
        # example cases
        self.cases_example = [
            self.Case("1.1.1.1", "1[.]1[.]1[.]1"),
            self.Case("255.100.50.0", "255[.]100[.]50[.]0")
        ]

    # defangIPaddr1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'defangIPaddr1: case: {i}'):
                act = self.solution.defangIPaddr1(Case.address)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
