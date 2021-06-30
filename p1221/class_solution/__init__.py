class Solution:
    def balancedStringSplit1(self, s: str) -> int:
        """
        Runtime: 28 ms, faster than 84.34% of Python3 online submissions for Split a String in Balanced Strings.
        Memory Usage: 14.2 MB, less than 39.07% of Python3 online submissions for Split a String in Balanced Strings.
        """
        # iterate and count quantity
        # when quantity is matched, count up
        qty_r = qty_l = 0
        cnt = 0
        for i in range(len(s)):
            if s[i] == 'R':
                qty_r += 1
            else:
                qty_l += 1
            if qty_r == qty_l:
                cnt += 1
                qty_r = qty_l = 0

        return cnt


