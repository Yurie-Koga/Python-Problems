class Solution:
    def numberOfSteps1(self, num: int) -> int:
        """
        Runtime: 32 ms, faster than 61.66% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
        Memory Usage: 14.2 MB, less than 65.79% of Python3 online submissions for Number of Steps to Reduce a Number to Zero.
        """
        # iterate
        cnt = 0
        while num > 0:
            num = num // 2 if num % 2 == 0 else num - 1
            cnt += 1
        return cnt
