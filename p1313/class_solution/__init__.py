from itertools import repeat
from typing import List


class Solution:
    def decompressRLElist1(self, nums: List[int]) -> List[int]:
        """
        Runtime: 64 ms, faster than 81.55% of Python3 online submissions for Decompress Run-Length Encoded List.
        Memory Usage: 14.8 MB, less than 24.48% of Python3 online submissions for Decompress Run-Length Encoded List.
        """
        # iterate + repeat
        res = []
        for i in range(0, len(nums), 2):
            res += repeat(nums[i + 1], nums[i])
        return res
