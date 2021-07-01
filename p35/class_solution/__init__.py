import bisect
from typing import List

"""
Bisect:
https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/
"""

class Solution:
    def searchInsert3(self, nums: List[int], target: int) -> int:
        """
        Runtime: 44 ms, faster than 91.14% of Python3 online submissions for Search Insert Position.
        Memory Usage: 15 MB, less than 52.73% of Python3 online submissions for Search Insert Position.
        """
        # edge cases + bisect : much faster
        if len(nums) == 0:
            return 0
        if nums[0] == target:
            return 0
        return bisect.bisect_left(nums, target)

    def searchInsert2(self, nums: List[int], target: int) -> int:
        """
        Runtime: 52 ms, faster than 46.02% of Python3 online submissions for Search Insert Position.
        Memory Usage: 15 MB, less than 52.73% of Python3 online submissions for Search Insert Position.
        """
        # bisect: find a position in list where an element needs to be inserted to keep the list sorted.

        return bisect.bisect_left(nums, target)

    def searchInsert1(self, nums: List[int], target: int) -> int:
        """
        Runtime: 36 ms, faster than 99.57% of Python3 online submissions for Search Insert Position.
        Memory Usage: 15 MB, less than 52.73% of Python3 online submissions for Search Insert Position.
        """
        # binary search + recursion with sliced list
        if len(nums) == 0:
            return 0

        i = len(nums) // 2
        if nums[i] == target:
            return i
        if target < nums[i]:
            return self.searchInsert1(nums[:i], target)
        else:
            i += 1  # move next
            res = self.searchInsert1(nums[i:], target)
            return res + i

    def searchInsert1_(self, nums: List[int], target: int) -> int:
        # binary search

        # edge case
        if target <= nums[0]:
            return 0
        if nums[-1] == target:
            return len(nums) - 1
        if nums[-1] < target:
            return len(nums)

        i = len(nums) // 2
        while i in range(1, len(nums) - 1):
            if target < nums[i]:
                if nums[i - 1] < target:
                    return i
                i = i // 2
            elif nums[i] == target:
                return i
            else:
                if target <= nums[i + 1]:
                    return i + 1
                i = i + (len(nums) - i) // 2

        return i
