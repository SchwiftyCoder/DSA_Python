"""
Determine the number of valid words in a given string S. A valid word contains at least 3 characters with only alphanumeric characters (i.e., the numbers 0-9, letters A-Z in either case), at least one vowel ('a', 'e', 'i', 'o', 'u'), and at least one consonant.

Example

Suppose s = "This is an example string 234".

Word	Is Valid	Reason
This	Yes	At least 3 characters, contains a vowel and a consonant
is	No	Less than 3 characters
an	No	Less than 3 characters
example	Yes	At least 3 characters, contains a vowel and a consonant
string	Yes	At least 3 characters, contains a vowel and a consonant
234	No	Does not contain a vowel or a consonant
Function Description

Complete the function countValidWords in the editor below.

countValidWords has the following parameter(s):

string s: a string to analyze
Returns

int: the number of valid words in s
Constraints

1 ≤ |s| ≤ 10^5
 
s consists of all available ASCII characters.
"""

class Solution:

    def countValidWords(self, s: str) -> int:
        vowels = "aeiou"
        consonants = "bcdfghjklmnpqrstvwxyz"
        validWordCount = 0

        # split str into a list (whitespace as sep)
        words = s.split()
        # print(f"raw word: {words}")
        # remove any non-alphanumeric characters
        wordsFiltered = [word for word in words if word.isalnum()]
        # print(f"words with alphanum only: {wordsFiltered}\n")
        # iterate through alphanmeric words and 
        for word in wordsFiltered:
            # convert to lower case
            wordLower = word.lower()
            # check if word has at least the following: 
            # of length 3, a vowel and a consonant
            if len(word) >= 3:
                # print(f"{word}", end="")
                hasVowel = any([s for s in wordLower if s in vowels])
                # print(f" => hasVowel: {hasVowel}")
                hasConsonant = any([s for s in wordLower if s in consonants])
                # print(f"        => hasConsonant: {hasConsonant}\n")
                # increase the count of valid words if all conditions are met
                if hasVowel and hasConsonant:
                    validWordCount += 1

        return validWordCount


sol = Solution()
print(sol.countValidWords("the dog21! is coming her123 wbblsd aieu"))