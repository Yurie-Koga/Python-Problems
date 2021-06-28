from typing import List


class Solution:
    def smallerNumbersThanCurrent1(self, nums: List[int]) -> List[int]:
        """
        Runtime: 540 ms, faster than 9.79% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
        Memory Usage: 14.3 MB, less than 71.60% of Python3 online submissions for How Many Numbers Are Smaller Than the Current Number.
        """
        # count the number of elements that is smaller than each element
        # set each count to return list
        res = []
        for i in range(len(nums)):
            res.append(sum(map(lambda x: x < nums[i], nums)))
        return res
