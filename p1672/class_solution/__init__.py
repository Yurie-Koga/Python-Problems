from typing import List


class Solution:
    def maximumWealth2(self, accounts: List[List[int]]) -> int:
        """
        Runtime: 52 ms, faster than 77.28% of Python3 online submissions for Richest Customer Wealth.
        Memory Usage: 14.4 MB, less than 26.62% of Python3 online submissions for Richest Customer Wealth.
        """
        return max([sum(x) for x in accounts])

    def maximumWealth1(self, accounts: List[List[int]]) -> int:
        """
        Runtime: 52 ms, faster than 77.28% of Python3 online submissions for Richest Customer Wealth.
        Memory Usage: 14.1 MB, less than 82.77% of Python3 online submissions for Richest Customer Wealth.
        """
        # sum of each accounts
        # get max
        res = []
        for i in range(len(accounts)):
            res.append(sum(accounts[i]))
        return max(res)
