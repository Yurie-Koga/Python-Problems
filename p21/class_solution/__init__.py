from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists3(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Runtime: 36 ms, faster than 77.18% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 14.2 MB, less than 60.30% of Python3 online submissions for Merge Two Sorted Lists.
        """
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1     # reorder to small -> large
            l1.next = self.mergeTwoLists3(l1.next, l2)  # read next node from the smaller ListNode
        return l1 or l2     # if l2 is None or reordered, return l1. otherwise (l1 is None), return l2 as it is

    def mergeTwoLists2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Runtime: 32 ms, faster than 92.11% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 14.4 MB, less than 29.29% of Python3 online submissions for Merge Two Sorted Lists.
        """
        dummy = ListNode(0)
        cur = dummy  # reference copy
        # compare: only when both ListNodes have element
        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        # rest: if either of ListNodes are None, just append to the result as they are already sorted
        cur.next = l1 or l2

        return dummy.next

    def mergeTwoLists1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Runtime: 32 ms, faster than 92.11% of Python3 online submissions for Merge Two Sorted Lists.
        Memory Usage: 14.4 MB, less than 29.29% of Python3 online submissions for Merge Two Sorted Lists.
        """
        # have 2 pointers for each ListNode
        # compare cur_val
        # l1 = l2 -> append bath to list, slide pointers and continue
        # l1 < l2 -> append l1, slide l1 pointer and continue
        # l1 > l2 -> append l2, slide l2 pointer and continue

        if l1 is None and l2 is None:
            return self.list_to_listnode([])

        if l1 is None:
            return l2
        if l2 is None:
            return l1

        res = []
        cur_val1 = l1.val
        cur_val2 = l2.val
        next_node1 = self.get_next_listnode(l1)
        next_node2 = self.get_next_listnode(l2)

        while next_node1 is not None or next_node2 is not None:
            if cur_val1 is None:
                res.append(cur_val2)
                cur_val2 = next_node2.val if next_node2 is not None else None
                next_node2 = self.get_next_listnode(next_node2)

            elif cur_val2 is None:
                res.append(cur_val1)
                cur_val1 = next_node1.val if next_node1 is not None else None
                next_node1 = self.get_next_listnode(next_node1)

            elif cur_val1 == cur_val2:
                res.append(cur_val1)
                res.append(cur_val2)
                cur_val1 = next_node1.val if next_node1 is not None else None
                cur_val2 = next_node2.val if next_node2 is not None else None
                next_node1 = self.get_next_listnode(next_node1)
                next_node2 = self.get_next_listnode(next_node2)

            elif cur_val1 < cur_val2:
                res.append(cur_val1)
                cur_val1 = next_node1.val if next_node1 is not None else None
                next_node1 = self.get_next_listnode(next_node1)

            else:
                res.append(cur_val2)
                cur_val2 = next_node2.val if next_node2 is not None else None
                next_node2 = self.get_next_listnode(next_node2)

        if cur_val1 is None:
            res.append(cur_val2)

        elif cur_val2 is None:
            res.append(cur_val1)

        elif cur_val1 == cur_val2:
            res.append(cur_val1)
            res.append(cur_val2)

        elif cur_val1 < cur_val2:
            res.append(cur_val1)
            res.append(cur_val2)

        else:
            res.append(cur_val2)
            res.append(cur_val1)

        return self.list_to_listnode(res)

    def list_to_listnode(self, l: List[int]) -> ListNode:
        return self.helper_list_to_listnode(l)

    def helper_list_to_listnode(self, l: List[int]) -> Optional[ListNode]:
        if len(l) == 0:
            return None
        elif len(l) == 1:
            return ListNode(val=l[0])
        else:
            cur = l.pop(0)
            return ListNode(val=cur, next=self.helper_list_to_listnode(l))

    def get_next_listnode(self, ln: ListNode) -> Optional[ListNode]:
        return ln.next if ln is not None else None

    def listnode_to_list(self, ln: ListNode) -> List[int]:
        if ln is None:
            return []

        res = []
        cur_val = ln.val
        next_node = self.get_next_listnode(ln)
        while next_node is not None:
            res.append(cur_val)
            cur_val = next_node.val
            next_node = self.get_next_listnode(next_node)

        res.append(cur_val)
        return res
