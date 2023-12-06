"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # if len(needle) > len(haystack):
        #     return -1
        # if not haystack or not needle: 
        #     return -1
        # if needle not in haystack:
        #     return -1

        # use string slicing
        needleSize = len(needle)
        index = 0
        needleOccurence = haystack[index:needleSize+index]
        while len(needleOccurence) == needleSize:
            # print(f"start: {index}\nend: {index+needleSize}\nstring: {needleOccurence}\n\n")
            if needleOccurence == needle: 
                return index 
            index += 1
            needleOccurence = haystack[index:needleSize+index]
        

        # for index in range(len(haystack)):
        #     # print(f"index start: {index}\nindex end {index + needleSize}\nchars: {haystack[index:needleSize+index]}\n")
        #     needleOccurence = haystack[index:needleSize+index]
        #     if needleOccurence == needle:
        #         # print(index)
        #         return index
        #     if len(needleOccurence) < needleSize:
        #         return -1
            

            
        return -1
            
solution = Solution()
print(solution.strStr("sabutsad", "sad"))
print(solution.strStr("", "df"))
print(solution.strStr("mississippi", "a"))