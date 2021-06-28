from typing import List


class Solution:
    def countMatches1(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        """
        Runtime: 248 ms, faster than 44.56% of Python3 online submissions for Count Items Matching a Rule.
        Memory Usage: 20.6 MB, less than 63.54% of Python3 online submissions for Count Items Matching a Rule.
        """
        # simply check if each value matches on rules

        res = 0
        for i in range(len(items)):
            if ruleKey == "type":
                input = items[i][0]
            elif ruleKey == "color":
                input = items[i][1]
            elif ruleKey == "name":
                input = items[i][2]

            res = res + 1 if self.is_match(input, ruleValue) else res

        return res

    def is_match(self, input: str, rule: str) -> bool:
        return input == rule
