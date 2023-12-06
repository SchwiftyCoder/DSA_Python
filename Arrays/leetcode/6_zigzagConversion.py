"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"
"""

class Solution:

    def convert(self, s: str, numRows: int) -> str:
        def displayGrid(grid, numRows, numColumns):
            for row in range(numRows): 
                for col in range(numColumns):  
                    print(f"[{grid[row][col]}]", end=" ") 
                print()

        numColumns = int(len(s)/2) 
        rows, cols = (numRows, numColumns) 
        grid = [['   ' for j in range(cols)] for i in range(rows)] 

        # display grid
        # displayGrid(grid, numRows, numColumns) 
        print()
        # generate vertical bars 
        start = 0
        end = numRows
        for col in range(0, numColumns, numRows-1):
            # grab the first numRows, skip numRows-2 and so on
            vertical_slice = s[start:end]  
            index = 0
            start = end + (numRows-2)
            end += (numRows+(numRows-2))
            for row in range(numRows):
                if index < len(vertical_slice):  
                    grid[row][col] = f" {vertical_slice[index]} "
                    index += 1  

        # displayGrid(grid, numRows, numColumns)

        # for diagonal print
        for col in range(1, numColumns-1, numRows-1):
            # generate one point per row/column
            print(col)

solution = Solution()
solution.convert("PAYPALISHIRING", 4)