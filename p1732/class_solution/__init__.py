from itertools import accumulate
from typing import List


class Solution:
    def largestAltitude1(self, gain: List[int]) -> int:
        """
        Runtime: 36 ms, faster than 60.57% of Python3 online submissions for Find the Highest Altitude.
        Memory Usage: 14.1 MB, less than 88.65% of Python3 online submissions for Find the Highest Altitude.
        """
        # add 0 at index = 0
        # accumulate + max
        gain.insert(0, 0)
        return max(accumulate(gain))
