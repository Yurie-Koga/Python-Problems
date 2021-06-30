class Solution:
    def removeOuterParentheses2(self, s: str) -> str:
        """
        Runtime: 28 ms, faster than 98.43% of Python3 online submissions for Remove Outermost Parentheses.
        Memory Usage: 14.3 MB, less than 59.75% of Python3 online submissions for Remove Outermost Parentheses.
        """
        # w/o popping (remove element) is much faster
        qty_r = qty_l = 0
        index_r = 0
        res = list(s)
        i = 0
        while i < len(res):
            if res[i] == '(':
                qty_r += 1
            else:
                qty_l += 1
            if qty_r == qty_l:
                res[i] = res[index_r] = ''
                index_r = i + 1

            i += 1

        return ''.join(res)

    def removeOuterParentheses1(self, s: str) -> str:
        """
        Runtime: 60 ms, faster than 9.65% of Python3 online submissions for Remove Outermost Parentheses.
        Memory Usage: 14.3 MB, less than 59.75% of Python3 online submissions for Remove Outermost Parentheses.
        """
        # iterate and count quantity: index_r = i
        # when quantity is matched, remove s[i] and s[index_r], reset index_r
        qty_r = qty_l = 0
        index_r = 0
        res = list(s)
        i = 0
        while i < len(res):
            if res[i] == '(':
                qty_r += 1
            else:
                qty_l += 1
            if qty_r == qty_l:
                res.pop(i)
                res.pop(index_r)
                i -= 2
                index_r = i + 1
            i += 1

        return ''.join(res)
