"""
151. Reverse Words in a String
Medium
Topics
Companies
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.

 

Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: s = "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.

"""

class Solution:
    def reverseWords(self, s: str) -> str:
        """
        split string into list based on ' '
        exclude empty strings from list
        reverse the list and convert back to string

        runs in O(n) time, best case
        """

        # s_to_list = [word for word in s.split() if word]
        s_to_list = s.split()
        return ' '.join(s_to_list[::-1])

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))
    print(sol.reverseWords("  hello world  "))