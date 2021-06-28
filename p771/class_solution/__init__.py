from typing import List


class Solution:
    def numJewelsInStones2(self, jewels: str, stones: str) -> int:
        """
        Runtime: 32 ms, faster than 62.23% of Python3 online submissions for Jewels and Stones.
        Memory Usage: 14.3 MB, less than 44.45% of Python3 online submissions for Jewels and Stones.
        """
        # map + count of chars in string
        return sum(map(jewels.count, stones))

    def numJewelsInStones1(self, jewels: str, stones: str) -> int:
        """
        Runtime: 28 ms, faster than 84.87% of Python3 online submissions for Jewels and Stones.
        Memory Usage: 14.3 MB, less than 11.72% of Python3 online submissions for Jewels and Stones.
        """
        # remove char from string
        # return len(original string) - len(trimmed string)
        res =stones
        for i in range(len(jewels)):
            res = res.replace(jewels[i], '')

        return len(stones) - len(res)
