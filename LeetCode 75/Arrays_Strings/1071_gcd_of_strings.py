"""
1071. Greatest Common Divisor of Strings
Easy
Topics
Companies
Hint
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"
Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""

"""

from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        """
        Approach:
            return

        Arguemnts:
            str1: the first string s
            str2: the second string t

        return:
            str that can eb used to generate both str1 and str2
        """

        str1_len = len(str1)
        str2_len = len(str2)

        # compute the gcd
        greatest_com_fac = gcd(str1_len, str2_len)

        # check if the gcd value generates str1 and str2
        predict_str1 = str2[:greatest_com_fac] * (str1_len // greatest_com_fac)
        predict_str2 = str2[:greatest_com_fac] * (str2_len // greatest_com_fac)

        return (
            str2[:greatest_com_fac]
            if predict_str1 == str1 and predict_str2 == str2
            else ""
        )


if __name__ == "__main__":
    sol = Solution()

    # returns ""
    print(sol.gcdOfStrings(str1="LEET", str2="CODE"))

    # returns "AB"
    print(sol.gcdOfStrings(str1="ABABAB", str2="ABAB"))

    # returns "ABC"
    print(sol.gcdOfStrings(str1="ABCABC", str2="ABC"))

    # returns ""
    print(sol.gcdOfStrings(str1="ABCDEF", str2="ABC"))

    # returns ""
    print(sol.gcdOfStrings(str1="AAAAAAAAA", str2="AAACCC"))
