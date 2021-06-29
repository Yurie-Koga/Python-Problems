import unittest
from collections import namedtuple

from p1678 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'command expect')
        # example cases
        self.cases_example = [
            self.Case(command="G()(al)", expect="Goal"),
            self.Case(command="G()()()()(al)", expect="Gooooal"),
            self.Case(command="(al)G(al)()()G", expect="alGalooG"),
        ]

    # interpret1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'interpret1: case: {i}'):
                act = self.solution.interpret1(Case.command)
                self.assertEqual(act, Case.expect)


if __name__ == '__main__':
    unittest.main()
