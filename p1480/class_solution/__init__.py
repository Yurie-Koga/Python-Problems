from typing import List


class Solution:
    def runningSum1(self, nums: List[int]) -> List[int]:
        """
        Runtime: 36 ms, faster than 86.06% of Python3 online submissions for Running Sum of 1d Array.
        Memory Usage: 14.3 MB, less than 68.20% of Python3 online submissions for Running Sum of 1d Array.
        """
        # loop + slicing a list (sublist)
        # list[a:b] = range(a, b) *b is not included
        for i in range(1, len(nums)):
            nums[i] = sum(nums[i - 1:i + 1])

        return nums
