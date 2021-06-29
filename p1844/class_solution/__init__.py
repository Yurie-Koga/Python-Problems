class Solution:
    def replaceDigits1(self, s: str) -> str:
        """
        Runtime: 32 ms, faster than 66.78% of Python3 online submissions for Replace All Digits with Characters.
        Memory Usage: 14.2 MB, less than 71.56% of Python3 online submissions for Replace All Digits with Characters.
        """
        # iterate + call shift() fxn
        res = list(s)
        for i in range(0, len(s) - 1, 2):
            res[i + 1] = self.shift(res[i], int(res[i + 1]))

        return ''.join(res)

    def shift(self, c: chr, amount: int) -> chr:
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z']
        return chars[chars.index(c) + amount]
