from typing import List


class Solution:
    def findCenter1(self, edges: List[List[int]]) -> int:
        """
        Runtime: 816 ms, faster than 50.10% of Python3 online submissions for Find Center of Star Graph.
        Memory Usage: 50.4 MB, less than 20.09% of Python3 online submissions for Find Center of Star Graph.
        """
        # no need to check all the elements in Lists as all the nodes should have the same center.
        # check the duplicate within the first and second node
        # then return the value as a center node

        return edges[0][0] if (edges[0][0] == edges[1][0] or edges[0][0] == edges[1][1]) else edges[0][1]
