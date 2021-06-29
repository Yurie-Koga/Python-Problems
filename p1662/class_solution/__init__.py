from functools import reduce
from typing import List


class Solution:
    def arrayStringsAreEqual1(self, word1: List[str], word2: List[str]) -> bool:
        """
        Runtime: 28 ms, faster than 86.49% of Python3 online submissions for Check If Two String Arrays are Equivalent.
        Memory Usage: 14.5 MB, less than 30.75% of Python3 online submissions for Check If Two String Arrays are Equivalent.
        """
        # combine by reduce + lambda
        return reduce(lambda x, y: x + y, word1) == reduce(lambda x, y: x + y, word2)
