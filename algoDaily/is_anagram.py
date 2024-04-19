"""
Is An Anagram (Easy)
Good evening, sQuancHY! Here's our prompt for today.

Understanding Anagrams: A Simple Definition
An anagram is a fascinating literary device where you can rearrange the letters of a word, phrase, or name to form another meaningful sequence. Think of it as a jigsaw puzzle made of letters. For example, the word "cinema" can be rearranged to form "iceman."

The Challenge: Detecting Anagrams
Problem Statement
Given two input strings like "cinema" and "iceman," your task is to implement a method called isAnagram(str1, str2). This method should return true if the given strings are anagrams of each other and false otherwise.

Constraints to Consider
Computational Limits
The length of both input strings will be less than or equal to 100,000.

Character Rules
The input strings will only contain alphanumeric characters (a-z, A-Z, 0-9).

Performance Expectations
The expected time complexity for this operation is O(nlogn).
The expected space complexity is O(n).
Empty Strings are Valid
The input strings can be empty. Imagine that as a puzzle with no pieces; it's trivially solvable!
Coding the Solution
Given the constraints and expectations, you'll need to think carefully about your algorithm. The aim is not just to solve the problem, but to solve it efficiently within the given computational and space boundaries.
"""

import unittest

class Solution:

    def is_anagram(self, str1, str2):
        """
        too expensive because
        time: O(nlogn)
        space: O(n + m)
        """

        str1 = sorted(str1.lower())
        str2 = sorted(str2.lower())
        
        return str1 == str2
    
    def is_anagram_v2(self, str1, str2):
        """
        build a dictionary out of str1, 1 pass, all keys are lower case
        traverse str2 and decrease count in dictionary

        if anagram, all values in dict must be 0
        else false

        """
        char_freq = {}
        for char in str1:
            char_to_lower = char.lower()
            if char_to_lower not in char_freq:
                char_freq[char_to_lower] = 1
            else:
                char_freq[char_to_lower] += 1

        for char in str2:
            char_to_lower = char.lower()
            if char_to_lower in char_freq:
                char_freq[char_to_lower] -= 1 
            else:
                return False

        for _, v in char_freq.items():
            if v != 0:
                return False
            
        return True
    
    def is_anagram_v3(self, str1, str2):
        """
        initialize an array of 256 size all elelemts 0 - ASCII characetr set
        each index from 0 through 255 corresponds to a character
        for char in str1
            convert to ASCII value using ord() and 
            then increase its value
        for char in str2:
            convert to ASCII value using ord() and 
            then decrease its count by 1

    
        traverse count array adn if any element is non-zero, return false else true
        
        """
        char_count = [0] * 256
        for char in str1:
            char_count[ord(char.lower())] += 1

        for char in str2:
            char_count[ord(char.lower())] -= 1


        return not any(char_count)


class Test(unittest.TestCase):
    
    def test_1(self): 
        assert Solution().is_anagram("Mary", "Army") == True
        print("PASSED: is_anagram('Mary', 'Army') should return False")

    def test_2(self):
        assert Solution().is_anagram("cinema", "iceman") == True
        print("PASSED: is_anagram('cinema', 'iceman') should return True")

    def test_3(self):
        assert Solution().is_anagram("jake", "jay") == False
        print("PASSED: is_anagram('jake', 'jay') should return False")


if __name__ == "__main__":
    unittest.main(verbosity=2)
    print("Nice job, 3/3 tests passed!")
