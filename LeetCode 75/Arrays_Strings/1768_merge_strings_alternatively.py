""""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
"""


class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        """ """

        mergedStr = ""
        char_index = 0
        while char_index < len(word1) and char_index < len(word2):
            mergedStr += word1[char_index] + word2[char_index]
            char_index += 1

        # append any remaingin characters

        mergedStr += (
            word1[char_index:] if len(word1) > len(word2) else word2[char_index:]
        )

        return mergedStr

    def mergeAlternately_v2(self, word1: str, word2: str) -> str:
        """
        a more pythonic way
        use a zip function to return a list
        and then merge the rest of the characters
        """
        mergedStr = "".join([a + b for a, b in zip(word1, word2)])
        # add the rest of the characters in word1 if it is longer than word2 else vice versa for word2
        mergedStr += (
            word1[len(word2) :] if len(word1) > len(word2) else word2[len(word1) :]
        )
        return mergedStr


sol = Solution()
# returns "apbqcr"
print(sol.mergeAlternately_v2(word1="abc", word2="pqr"))
print(sol.mergeAlternately(word1="abc", word2="pqr"))

# returns "apbqcd"
print(sol.mergeAlternately_v2(word1="abcd", word2="pq"))
print(sol.mergeAlternately(word1="abcd", word2="pq"))

# returns "apbqrs"
print(sol.mergeAlternately_v2(word1="ab", word2="pqrs"))
print(sol.mergeAlternately_v2(word1="ab", word2="pqrs"))
