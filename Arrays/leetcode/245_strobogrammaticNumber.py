"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false

Example 4:
Input: num = "1"
Output: true
"""

class Solution:

   
    def isStroboGrammatic(self, number: int) -> bool:
        # a list of all non-strobogrammatic numbers
        nonStrobogrammatic = ["2", "3", "4", "5", "7"]

        # if the number contains anyone of the characters above, return false 
        for digit in number:
            if digit in nonStrobogrammatic: 
                return False
            
        return True



solution = Solution()
print(solution.isStroboGrammatic("69"))   # Should return True
print(solution.isStroboGrammatic("88"))   # Should return True
print(solution.isStroboGrammatic("962"))  # Should return False
print(solution.isStroboGrammatic("1"))    # Should return True
print(solution.isStroboGrammatic("101"))  # Should return True
print(solution.isStroboGrammatic("818"))  # Should return True
print(solution.isStroboGrammatic("8008")) # Should return True
print(solution.isStroboGrammatic("2"))    # Should return False

print(solution.isStroboGrammatic("609"))  # Should return False 
