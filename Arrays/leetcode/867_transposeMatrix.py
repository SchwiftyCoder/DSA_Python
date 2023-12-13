"""
867. Transpose Matrix

Given a 2D integer array matrix, return the transpose of matrix.

The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]
Example 2:

Input: matrix = [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
-109 <= matrix[i][j] <= 109
"""

from typing import List
class Solution:

    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        # create n columns and replicate it an x number of times
        # transposeMatrix = [[0]*col] * row 
        transposeMatrix = [[0 for _ in range(row)] for _ in range(col)]
        

        # matric transposition is such that (x, y) becomes (y, x)
        for c in range(col):
            for r in range(row):
                # print(f"matrix[{c}][{r}]: {matrix[c][r]}")
                transposeMatrix[c][r] = matrix[r][c]
                print(transposeMatrix)

        print()
        return transposeMatrix 
    
sol = Solution()
print(sol.transpose([[1,2,3],[4,5,6],[7,8,9]]))
