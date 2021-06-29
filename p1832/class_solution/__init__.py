class Solution:
    def checkIfPangram1(self, sentence: str) -> bool:
        """
        Runtime: 28 ms, faster than 85.64% of Python3 online submissions for Check if the Sentence Is Pangram.
        Memory Usage: 14.1 MB, less than 90.15% of Python3 online submissions for Check if the Sentence Is Pangram.
        """
        # remove duplicate chars
        # return len() == 26
        return len(set(sentence)) == 26
