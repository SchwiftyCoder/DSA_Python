"""
67. Add Binary 
Given two binary strings a and b, return their sum as a binary string.


Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

"""

class Solutin:

    """
    Convert Binary to Decimal:

It iterates over each binary string (a and b), converting them to their decimal equivalents (aBase10 and bBase10).
The conversion is done by iterating from the end of the string and adding 2^index to the sum if the digit is '1'.
Addition of Decimal Numbers:

The decimal equivalents are then added together to get the sum in base 10.
Convert Sum Back to Binary:

The sum is converted back to a binary string using repeated division by 2, gathering remainders.
Efficiency and Big O Analysis:

The algorithm's time complexity is O(n), where n is the length of the longer binary string. This is because it iterates over each string once for conversion.
However, it involves multiple loops and conversions, making it less efficient in terms of practical runtime compared to a direct bit-by-bit addition approach.
    """
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        def toBase10(binaryStr: str) -> int:
            base10 = 0
            for right in range(len(binaryStr)-1, -1, -1):
                if binaryStr[(len(binaryStr)-1) - right] != "0": 
                    base10 += pow(2, right)
            return base10
        
        aBase10 = toBase10(a)
        bBase10 = toBase10(b)
        sum = aBase10 + bBase10

        if sum == 0:
            return "0"

        toBaseTwo = ""
        while sum != 0:
            remainder = sum % 2
            toBaseTwo = str(remainder) + toBaseTwo
            sum = sum // 2

        print(toBaseTwo)
        return toBaseTwo




    """
    
    """
    def addBinary_v2(self, a: str, b: str) -> str:
        pass

solution = Solution()
# solution.addBinary("11", "1")
solution.addBinary("1010", "1011")
# solution.addBinary("0", "0")
# solution.addBinary("1", "1")