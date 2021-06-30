import re


class Solution:
    def halvesAreAlike2(self, s: str) -> bool:
        """
        Runtime: 36 ms, faster than 61.40% of Python3 online submissions for Determine if String Halves Are Alike.
        Memory Usage: 14.2 MB, less than 61.53% of Python3 online submissions for Determine if String Halves Are Alike.
        """
        # slice into two lists
        # compare count of vowels
        vowels = list('aeiou')
        a = list(s.lower())[:len(s) // 2]
        b = list(s.lower())[len(s) // 2:]

        cnt_a = cnt_b = 0
        for c in vowels:
            cnt_a += a.count(c)
            cnt_b += b.count(c)

        return cnt_a == cnt_b

    def halvesAreAlike1(self, s: str) -> bool:
        """
        Runtime: 44 ms, faster than 17.76% of Python3 online submissions for Determine if String Halves Are Alike.
        Memory Usage: 14.6 MB, less than 7.17% of Python3 online submissions for Determine if String Halves Are Alike.
        """

        # slice into two lists
        # remove vowels by regex and compare length

        a = list(s)[:len(s) // 2]
        b = list(s)[len(s) // 2:]
        pattern = '(?i)a|e|i|o|u'
        return len(re.sub(pattern, '', str(a))) == len(re.sub(pattern, '', str(b)))
