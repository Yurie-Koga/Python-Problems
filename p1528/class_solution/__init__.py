from typing import List


class Solution:
    def restoreString2(self, s: str, indices: List[int]) -> str:
        """
        Runtime: 56 ms, faster than 59.02% of Python3 online submissions for Shuffle String.
        Memory Usage: 14.4 MB, less than 19.82% of Python3 online submissions for Shuffle String.
        """
        # zip two lists -> [(chr, index), (), ()]
        # sort zip
        # extract only chr order by index
        pairs = zip(indices, s)
        return ''.join([v for (k, v) in sorted(pairs, key=lambda x: x[0])])

    def restoreString1(self, s: str, indices: List[int]) -> str:
        """
        Runtime: 44 ms, faster than 98.60% of Python3 online submissions for Shuffle String.
        Memory Usage: 14.4 MB, less than 19.82% of Python3 online submissions for Shuffle String.
        """

        # zip two lists
        # store zip to dict
        # extract values order by indices (key)

        dict_pair = dict(zip(indices, s))
        return ''.join([v for (k, v) in sorted(dict_pair.items())])
