from typing import List


class Solution:
    def sortSentence1(self, s: str) -> str:
        """
        Runtime: 28 ms, faster than 84.38% of Python3 online submissions for Sorting the Sentence.
        Memory Usage: 14.3 MB, less than 46.06% of Python3 online submissions for Sorting the Sentence.
        """
        # split by a space -> list
        # read through the list and store to dictionary<index, string>
        # sort the dict by key and append value to string
        words = s.split(' ')
        word_dict = {}
        for i in range(len(words)):
            word_dict[words[i][len(words[i]) - 1]] = words[i][:-1]

        return ' '.join([v for (k, v) in sorted(word_dict.items())])


