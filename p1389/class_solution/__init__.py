from typing import List


class Solution:
    def createTargetArray1(self, nums: List[int], index: List[int]) -> List[int]:
        """
        Runtime: 28 ms, faster than 92.44% of Python3 online submissions for Create Target Array in the Given Order.
        Memory Usage: 14.3 MB, less than 12.17% of Python3 online submissions for Create Target Array in the Given Order.
        """
        # iterate + insert
        res = []
        for i in range(len(nums)):
            if i != index[i]:
                res.insert(index[i], nums[i])
            else:
                res.append(nums[i])

        return res
