from typing import List


class Solution:
    def maxProduct2(self, nums: List[int]) -> int:
        """
        Runtime: 48 ms, faster than 84.69% of Python3 online submissions for Maximum Product of Two Elements in an Array.
        Memory Usage: 14.3 MB, less than 43.04% of Python3 online submissions for Maximum Product of Two Elements in an Array.
        """
        # sort descending
        # return nums[0] * nums[1]
        nums.sort(reverse=True)
        return (nums[0] - 1) * (nums[1] - 1)

    def maxProduct1(self, nums: List[int]) -> int:
        """
        Runtime: 40 ms, faster than 98.88% of Python3 online submissions for Maximum Product of Two Elements in an Array.
        Memory Usage: 14.3 MB, less than 71.58% of Python3 online submissions for Maximum Product of Two Elements in an Array.
        """
        # pick up the largest two elements by max
        # return product of them
        a = nums.pop(nums.index(max(nums)))
        b = nums.pop(nums.index(max(nums)))

        return (a - 1) * (b - 1)
