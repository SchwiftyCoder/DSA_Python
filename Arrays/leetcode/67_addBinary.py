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
        Add two binary strings and return their sum as a binary string.

        The method first equalizes the lengths of the two binary strings by padding them with leading zeros. 
        It then iterates over these strings from the least significant digit (rightmost) to the most significant digit (leftmost),
        adding corresponding digits along with any carry from the previous addition. 
        The sum for each digit is calculated and the carry is propagated as needed. 
        The final binary sum is constructed in reverse order and returned.

        Time Complexity: O(n), where n is the length of the longer binary string.
        Space Complexity: O(n), for storing the result.

        Parameters:
        a (str): The first binary string.
        b (str): The second binary string.

        Returns:
        str: The sum of the two binary strings as a binary string.
        """

    def addBinary_v2(self, a: str, b: str) -> str:
        # get the largest length
        max_length = max(len(a), len(b))

        # fill any left spaces with 0
        a = a.zfill(max_length)
        b = b.zfill(max_length)

        print(a)
        print(b)

        # stores the sum
        binarySum = []
        carryOver = 0

        # we can now step through any pair of elements from from strings starting at the end

        for index in range(len(a)-1, -1, -1):
            sum = int(a[index]) + int(b[index]) + carryOver
            print(f"raw sum: {sum} | ", end="")
            carryOver = sum // 2
            print(f"carry: {carryOver}", end="")
            sum = sum % 2 
            print(f" | binary sum: {sum}")
            binarySum.append(str(sum))
           
        # add the last carry if is a 1
        if carryOver == 1:
            binarySum.append(str(carryOver))

        print(''.join(reversed(binarySum)))



solution = Solution()
# solution.addBinary("11", "1")
# solution.addBinary("1010", "1011")
# solution.addBinary("0", "0")
# solution.addBinary("1", "1")


# solution.addBinary_v2("101111", "111")
solution.addBinary_v2("11", "1")
# solution.addBinary("0", "0")