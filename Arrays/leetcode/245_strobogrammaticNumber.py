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

    """
    Approach: 
        keep a log all non strobo numbers 
        loop through number string
        if a character from the string is in the non strobo numbers, return false

        iterates throught the string n times, thus O(n)
    """
    def isStroboGrammatic(self, number: int) -> bool:
        # a list of all non-strobogrammatic numbers
        nonStrobogrammatic = ["2", "3", "4", "5", "7"]

        # if the number contains anyone of the characters above, return false 
        for digit in number:
            if digit in nonStrobogrammatic: 
                return False
            
        return True
    

    """
    optimized approach
    two pointers: at both ends initially and check against dictinary
    invrease left pointer
    decrease right pinter
    left pointer must never surpase right pointer but can be equal to it

    ierates through the string n/2 times but essentially still O(n)
    """
    def isStrobogrammatic_v2(self, num: str) -> bool:
        mirrorPairs = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6"
        } 

        left, right = 0, len(num) - 1
        while left <= right:
            # print(f"left: {left}\nright: {right}\n")
            # digit in number is not in dictionary keys
            if num[left] not in mirrorPairs or num[right] not in mirrorPairs:
                return False
            # digit is in dictionary but does not match any value
            if mirrorPairs[num[left]] != num[right]:
                return False
            left += 1
            right -= 1 

        return True          
            




solution = Solution()
# print(solution.isStroboGrammatic("69"))   # Should return True
# print(solution.isStroboGrammatic("88"))   # Should return True
# print(solution.isStroboGrammatic("962"))  # Should return False
# print(solution.isStroboGrammatic("1"))    # Should return True
# print(solution.isStroboGrammatic("101"))  # Should return True
# print(solution.isStroboGrammatic("818"))  # Should return True
# print(solution.isStroboGrammatic("8008")) # Should return True
# print(solution.isStroboGrammatic("2"))    # Should return False 
# print(solution.isStroboGrammatic("609"))  # Should return False 


print()
print(solution.isStrobogrammatic_v2("69"))   # Should return True
print(solution.isStrobogrammatic_v2("88"))   # Should return True
print(solution.isStrobogrammatic_v2("962"))  # Should return False
print(solution.isStrobogrammatic_v2("1"))    # Should return True
print(solution.isStrobogrammatic_v2("101"))  # Should return True
print(solution.isStrobogrammatic_v2("818"))  # Should return True
print(solution.isStrobogrammatic_v2("8008")) # Should return True
print(solution.isStrobogrammatic_v2("2"))    # Should return False 
print(solution.isStrobogrammatic_v2("609"))  # Should return False 


