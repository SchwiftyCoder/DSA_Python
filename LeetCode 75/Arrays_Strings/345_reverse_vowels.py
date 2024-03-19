"""
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 
Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
"""


class Solution:
    def reverseVowels(self, s: str) -> str:
        """

        universal step:
            convert string to list
            O(n) time
            O(n) space

        Approach 1:
            1 pass through string
            O(n) time
            O(1) space only 2 variables are used, modifies elements in place
        use two pointers
        vowels = "aAeEiIoOuU"
        p1 starts at index 0
        p2 starts at index n-1
        while p1 < p2
            if both chars are in vowels,
                swap
                increase p1
                decrease p2
            else if p1 is and p2 is not
                decrease p2
            else if p1 is not and p2 is
                increase p1
            else:
                increase p1
                decrease p2
        """
        
        chars = list(s)
        p1 = 0
        p2 = len(s) - 1
        vowels = "aAeEiIoOuU"
        while p1 < p2:
            if chars[p1] in vowels and chars[p2] in vowels:
                chars[p1], chars[p2] = chars[p2], chars[p1]
                p1 += 1
                p2 -= 1
            elif chars[p1] in vowels and chars[p2] not in vowels:
                p2 -= 1
            elif chars[p1] not in vowels and chars[p2] in vowels:
                p1 += 1
            else:
                p1 += 1
                p2 -= 1

        return ''.join(chars)
            


    def reverseVowels_v2(self, s: str) -> str:
        """
        Approach 2:
            2 passes
            O(n) time where n is the number of elements
            O(n) space where n is the number of vowels
        convert string to list
        loop 1: log the index positins of all vowels starting at index 0
        loop 2: starting at the last char in the list, replace the vowels in the string starting at index 0
        """
        pass

    def reverseVowels_v3(self, s: str) -> str:
        """
        Approach 3:
            2 passes
            O(n) time where n is the number of elements
            O(n) space where n is the number of vowels
        iterate through the string and push all vowels to stack (will automatically be in reverse order)
        iterate through the string again: when a vowel is encountered, pop off the stack and replace
        """
        pass
