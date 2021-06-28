"""
Bitwise XOR in Python:
https://realpython.com/python-bitwise-operators/#:~:text=the%20bitwise%20xor%20operator%20(%5E)%20doesn%E2%80%99t%20have%20a%20logical%20counterpart%20in%20python
"""


class Solution:
    def xorOperation1(self, n: int, start: int) -> int:
        """
        Runtime: 32 ms, faster than 62.50% of Python3 online submissions for XOR Operation in an Array.
        Memory Usage: 14 MB, less than 98.59% of Python3 online submissions for XOR Operation in an Array.
        """
        # simply iterate
        res = start
        for i in range(1, n):
            res ^= start + (2 * i)
        return res
