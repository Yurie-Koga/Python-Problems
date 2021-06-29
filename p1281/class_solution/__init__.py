import math
from functools import reduce


class Solution:
    def subtractProductAndSum3(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 56.89% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        Memory Usage: 14.3 MB, less than 10.87% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        """
        # math.prod
        nums = list(map(int, str(n)))
        return math.prod(nums) - sum(nums)

    def subtractProductAndSum2(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 56.89% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        Memory Usage: 14.1 MB, less than 69.39% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        """
        # map to int and convert to list
        # reduce + lambda

        nums = list(map(int, str(n)))
        return reduce((lambda x, y: x * y), nums) - reduce((lambda x, y: x + y), nums)

    def subtractProductAndSum1(self, n: int) -> int:
        """
        Runtime: 32 ms, faster than 56.89% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        Memory Usage: 14.3 MB, less than 39.71% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
        """
        # iterate to int
        # reduce + lambda

        nums = [int(x) for x in str(n)]
        return reduce((lambda x, y: x * y), nums) - reduce((lambda x, y: x + y), nums)
