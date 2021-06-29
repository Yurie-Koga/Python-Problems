class Solution:
    def interpret1(self, command: str) -> str:
        """
        Runtime: 32 ms, faster than 57.69% of Python3 online submissions for Goal Parser Interpretation.
        Memory Usage: 14.1 MB, less than 66.45% of Python3 online submissions for Goal Parser Interpretation.
        """
        # dict: set patterns
        # iterate + str.replace
        patterns = {'()': 'o', '(al)': 'al'}
        for (k, v) in patterns.items():
            command = command.replace(k, v)

        return command
