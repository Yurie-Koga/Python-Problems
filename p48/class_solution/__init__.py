from typing import List


class Solution:
    # def rotate1(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    def rotate2(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 32 ms, faster than 86.11% of Python3 online submissions for Rotate Image.
        Memory Usage: 14.2 MB, less than 59.91% of Python3 online submissions for Rotate Image.
        """
        # ~a : invert(a)
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[j][~i], matrix[~i][~j], matrix[~j][i] = matrix[~j][i], matrix[i][j], matrix[j][~i], matrix[~i][~j]
        return matrix

    def rotate1(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        Runtime: 28 ms, faster than 95.80% of Python3 online submissions for Rotate Image.
        Memory Usage: 14.2 MB, less than 59.91% of Python3 online submissions for Rotate Image.
        """
        # image :
        # - recursively swap/slide toward to the clockwise -> actually 4 times
        # - multiple swaps can be done a single line in python
        #
        # how to downsize into inside layers?
        # n: 4 > 2 > 0. 5 > 3 > 1. n > n'=n//2 > n''=n'//2
        # eg. (n=3)
        # [0][0] -> [0][2]
        # [0][2] -> [2][2]
        # [2][2] -> [2][0]
        # [2][0] -> [0][0]
        # eg. (n=4)
        # [0][0] -> [0][3]
        # [0][3] -> [3][3]
        # [3][3] -> [3][0]
        # [3][0] -> [0][0]
        #   [1][1] -> [1][2]
        #   [1][2] -> [2][2]
        #   [2][2] -> [2][1]
        #   [2][1] -> [1][1]

        # move only corner
        # n = len(matrix)
        # max = n // 2 - 0 + 1
        # r, c = 0, 0
        # matrix[r][max], matrix[max][max], matrix[max][c], matrix[r][c] \
        #     = matrix[r][c], matrix[r][max], matrix[max][max], matrix[max][c]

        n = len(matrix)
        for r in range(n // 2):
            i = 0
            for c in range(r, n - 1 - r):
                max_row = n - r - 1
                max_col = n - c - 1
                #   top-left,    top-right, bottom-right, bottom-left
                # = bottom-left, top-left,  top-right,    bottom-right
                matrix[r][c], matrix[r + i][max_row], matrix[max_row][max_col], matrix[max_col][r] \
                    = matrix[max_col][r], matrix[r][c], matrix[r + i][max_row], matrix[max_row][max_col]
                i += 1
        return matrix
