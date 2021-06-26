import unittest
from collections import namedtuple

from p21 import class_solution


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = class_solution.Solution()
        self.Case = namedtuple('Case', 'l1 l2 expect')
        # example cases
        self.cases_example = [
            self.Case(self.solution.list_to_listnode([1, 2, 4]),
                      self.solution.list_to_listnode([1, 3, 4]),
                      self.solution.list_to_listnode([1, 1, 2, 3, 4, 4])),
            self.Case(self.solution.list_to_listnode([]),
                      self.solution.list_to_listnode([]),
                      self.solution.list_to_listnode([])),
            self.Case(self.solution.list_to_listnode([]),
                      self.solution.list_to_listnode([0]),
                      self.solution.list_to_listnode([0]))
        ]
        # additional cases
        self.cases_other = [
            self.Case(self.solution.list_to_listnode([2]),
                      self.solution.list_to_listnode([1]),
                      self.solution.list_to_listnode([1, 2])),
            self.Case(self.solution.list_to_listnode([-9, 3]),
                      self.solution.list_to_listnode([5, 7]),
                      self.solution.list_to_listnode([-9, 3, 5, 7])),
        ]
        # my cases
        self.cases_mine = [
            self.Case(self.solution.list_to_listnode([2]),
                      self.solution.list_to_listnode([]),
                      self.solution.list_to_listnode([2])),
            self.Case(self.solution.list_to_listnode([2, 3]),
                      self.solution.list_to_listnode([]),
                      self.solution.list_to_listnode([2, 3])),
        ]

    def test_list_to_listnode(self):
        list = [1, 2]
        listnode = self.solution.list_to_listnode(list)
        cur_val = listnode.val
        next_node = self.solution.get_next_listnode(listnode)
        while next_node is not None:
            print(f'curVal: {cur_val}, next val: {next_node.val}')
            cur_val = next_node.val
            next_node = self.solution.get_next_listnode(next_node)

        print(f'curVal: {cur_val}, next val: None')

    def test_listnode_to_list(self):
        list = [1, 2]
        listnode = self.solution.list_to_listnode(list)
        new_list = self.solution.listnode_to_list(listnode)
        print(str(new_list))

    # mergeTwoLists1
    def test_examples1(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'case: {i}'):
                act = self.solution.mergeTwoLists1(Case.l1, Case.l2)
                self.assertEqual(self.solution.listnode_to_list(act), self.solution.listnode_to_list(Case.expect))

    def test_others1(self):
        for i, Case in enumerate(self.cases_other):
            with self.subTest(f'case: {i}'):
                act = self.solution.mergeTwoLists1(Case.l1, Case.l2)
                self.assertEqual(self.solution.listnode_to_list(act), self.solution.listnode_to_list(Case.expect))

    # mergeTwoLists2
    def test_examples2(self):
        for i, Case in enumerate(self.cases_example):
            with self.subTest(f'case: {i}'):
                act = self.solution.mergeTwoLists2(Case.l1, Case.l2)
                self.assertEqual(self.solution.listnode_to_list(act), self.solution.listnode_to_list(Case.expect))

    def test_others2(self):
        for i, Case in enumerate(self.cases_other):
            with self.subTest(f'case: {i}'):
                act = self.solution.mergeTwoLists2(Case.l1, Case.l2)
                self.assertEqual(self.solution.listnode_to_list(act), self.solution.listnode_to_list(Case.expect))

    def test_mine2(self):
        for i, Case in enumerate(self.cases_mine):
            with self.subTest(f'case: {i}'):
                act = self.solution.mergeTwoLists2(Case.l1, Case.l2)
                self.assertEqual(self.solution.listnode_to_list(act), self.solution.listnode_to_list(Case.expect))


if __name__ == '__main__':
    unittest.main()
