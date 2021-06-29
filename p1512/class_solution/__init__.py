from typing import List


class Solution:
    def numIdenticalPairs1(self, nums: List[int]) -> int:
        """
        Runtime: 32 ms, faster than 79.02% of Python3 online submissions for Number of Good Pairs.
        Memory Usage: 14.2 MB, less than 70.47% of Python3 online submissions for Number of Good Pairs.
        """
        # use double loop
        # if good pair, count up
        cnt = 0
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    cnt += 1

        return cnt
