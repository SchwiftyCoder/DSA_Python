"""
205 Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true
 

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.
"""

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(s):
            return False
        
        st_dict = {}

        for sKey, tValue in zip(s, t):
            print(f"s key: {sKey}, t value: {tValue}")
            print(f"dict values: {st_dict.values()}")
            if sKey not in st_dict:
                if tValue in st_dict.values():
                    print(f"{sKey}, {tValue} mismatch\n")
                    return False
                st_dict[sKey] = tValue
            elif st_dict[sKey] != tValue:
                print(f"{sKey}, {tValue} mismatch\n")
                  
            
            
            print(f"partial dictionary: {st_dict}\n")

        print(st_dict)


        



solution = Solution()
# solution.isIsomorphic("badc", "baba")
# solution.isIsomorphic("egg", "eda")
# solution.isIsomorphic("egg", "add")
solution.isIsomorphic("foo", "bar")
# solution.isIsomorphic("paper", "title")
