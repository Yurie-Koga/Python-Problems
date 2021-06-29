class Solution:
    def truncateSentence1(self, s: str, k: int) -> str:
        """
        Runtime: 32 ms, faster than 56.51% of Python3 online submissions for Truncate Sentence.
        Memory Usage: 14.2 MB, less than 75.82% of Python3 online submissions for Truncate Sentence.
        """
        # split by a space -> list
        # slice
        words = s.split(' ')
        return ' '.join(words[:k])
