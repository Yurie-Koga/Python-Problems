from typing import List


class Solution:
    def flipAndInvertImage2(self, image: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 52 ms, faster than 57.83% of Python3 online submissions for Flipping an Image.
        Memory Usage: 14.5 MB, less than 22.46% of Python3 online submissions for Flipping an Image.
        """
        # map + list comprehension
        image = [list(reversed(x)) for x in image]
        return [list(map(lambda x: 0 if x == 1 else 1, group)) for group in image]

    def flipAndInvertImage1(self, image: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 40 ms, faster than 98.89% of Python3 online submissions for Flipping an Image.
        Memory Usage: 14.5 MB, less than 22.46% of Python3 online submissions for Flipping an Image.
        """
        # w/o map
        # reverse
        # invert by []
        # for i in range(len(image)):
        #     image[i].reverse()
        #

        image = [list(reversed(x)) for x in image]
        return [[0 if x == 1 else 1 for x in group] for group in image]
