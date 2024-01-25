"""
242. Valid Anagram 
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

class solution:

    def isAnagram(self, s: str, t: str):

        if len(s) != len(t):
            return False
        
        s_dict = {}
        t_dict = {}

        for index in range(len(s)):
            # build dictionaries
            # check if the element is in the diction
            if s[index] in s_dict:
                s_dict[s[index]] += 1
            else:
                s_dict[s[index]] = 1

            # build the second dictionary
            if t[index] in t_dict:
                t_dict[t[index]] += 1
            else:
                t_dict[t[index]] = 1

            
        # compare the two dictionarys
        return s_dict == t_dict        

    
solution = solution()
print(solution.isAnagram_v2("ac", "bb"))