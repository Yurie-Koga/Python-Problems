from itertools import chain
from typing import List


class Solution:
    def shuffle2(self, nums: List[int], n: int) -> List[int]:
        """
        Runtime: 52 ms, faster than 96.14% of Python3 online submissions for Shuffle the Array.
        Memory Usage: 14.6 MB, less than 15.23% of Python3 online submissions for Shuffle the Array.
        """
        # slice and zip: [(1, 2), (3, 4)]
        # convert tuple into a list by chain
        return list(chain(*zip(nums[:n], nums[n:])))

    def shuffle1(self, nums: List[int], n: int) -> List[int]:
        """
        Runtime: 52 ms, faster than 96.14% of Python3 online submissions for Shuffle the Array.
        Memory Usage: 14.4 MB, less than 48.07% of Python3 online submissions for Shuffle the Array.
        """
        # slice into 2 lists
        # read through them and pick up values one by one
        nums1 = nums[:n]
        nums2 = nums[n:]
        res = []
        for i in range(n):
            res.append(nums1[i])
            res.append(nums2[i])

        return res
