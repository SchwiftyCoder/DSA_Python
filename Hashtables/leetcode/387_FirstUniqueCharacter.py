"""
387. First Unique Character in a String 

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1
 

Constraints:

1 <= s.length <= 105
s consists of only lowercase English letters.
"""


class Solution:

    """
    add element and occurence count to dictionary
    """

    def firstUniqueChar(self, s: str) -> int:
        dict = {}
        for char in s:
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1

        # alternative way to build dictionary
        # .get returns 0 is key does not exists in dictionary
        # + 1 updates the current count of the character by 1
        charCount = {}
        for char in s:
            charCount[char] = charCount.get(char, 0) + 1

        for index, char in enumerate(s):
            if charCount[char] == 1:
                return index

        return -1


sol = Solution()
print(sol.firstUniqueChar("aabb"))
print(sol.firstUniqueChar("leetcode"))
print(sol.firstUniqueChar("loveleetcode"))
