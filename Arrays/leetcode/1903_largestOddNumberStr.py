"""
1903. Largest Odd Number in String

You are given a string num, representing a large integer. Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: num = "52"
Output: "5"
Explanation: The only non-empty substrings are "5", "2", and "52". "5" is the only odd number.
Example 2:

Input: num = "4206"
Output: ""
Explanation: There are no odd numbers in "4206".
Example 3:

Input: num = "35427"
Output: "35427"
Explanation: "35427" is already an odd number.
"""

class Solution:

    """
    solution runs in O(n) time where n is the length of the string

    """
    def largestOddNumber(self, num: str) -> str:
        # check if the last digit of num best case scenario O(1) if last digit is odd
        # if (int(num) % 10) % 2 != 0:
        #     print(num)
        #     return num
        
        largestOdd = "" 
        substr = ""
        for char in num:
            substr += char
            if int(char) % 2 != 0: #char is odd
                # print(f"char: {char} is odd\noverall odd: {substr}\n") 
                largestOdd = substr

        # print(f"largest odd: {largestOdd}\n")
        print(largestOdd)
        return largestOdd
    
    """
    Apporach 2: use string slicing with start 0 and stop first occurence of odd number
    """
    def largestOddNumber_v2(self, num: str) -> str:
        # traverse the list in reverse order
        largestOdd = ""
        for index in range(len(num) - 1, -1, -1):
            print(f"checking {num[index]}")
            if int(num[index]) % 2 != 0:
                print(f"{num[index]} is odd\n")
                largestOdd = num[:index+1]
                break
                # return num[:index+1]
        print(largestOdd)
        # else return the empty string
        return ""
        


solution = Solution()
# solution.largestOddNumber("52")
# solution.largestOddNumber("4967210")
# solution.largestOddNumber("13542718")
# solution.largestOddNumber("19812")
# solution.largestOddNumber("22")
# solution.largestOddNumber("112")

print()

# solution.largestOddNumber_v2("52")
# solution.largestOddNumber_v2("4967210")
# solution.largestOddNumber_v2("13542718")
solution.largestOddNumber_v2("19812")
# solution.largestOddNumber_v2("22")
# solution.largestOddNumber_v2("112")