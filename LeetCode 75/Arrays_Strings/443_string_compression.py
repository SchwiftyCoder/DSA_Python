"""
443. String Compression 
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space. 

Example 1:

Input: chars = ["a","a","b","b","c","c","c"]
Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation: The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
Example 2:

Input: chars = ["a"]
Output: Return 1, and the first character of the input array should be: ["a"]
Explanation: The only group is "a", which remains uncompressed since it's a single character.
Example 3:

Input: chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output: Return 4, and the first 4 characters of the input array should be: ["a","b","1","2"].
Explanation: The groups are "a" and "bbbbbbbbbbbb". This compresses to "ab12".
"""
from typing import List
class Solution: 
        
    def compress_v2(self, chars: List[str]) -> int:
        """
        use 2 pointers: i and j, 
        if character at both i and j are equal:
            increase character frequency count
            if length of char freq count is greater than 1
                enumrate over the count and assign character to the chars
            else:
                simply add the updated char count to after the char being counted
        else:
            set i to j sinc a new char is encountered
            reset char freq count to 1
        always increase j by 1


        Return:
            the length of the string, forget aobut the rest of the characters
        """
        i = 0
        j = 1
        n = len(chars)
        charCount = 1
        lastIndex = 0
        while j < n: 
            if chars[i] == chars[j]:
                charCount += 1
                if len(str(charCount)) > 1: 
                    for index, value in enumerate(str(charCount)):
                        chars[i + (index + 1)] = str(value)  
                        lastIndex = index + i + 1
                else:
                    chars[i + 1] = str(charCount) 
                    lastIndex = i + 1
            else: 
                i = j
                charCount = 1 
            j += 1

        print(chars)
        print(f"last index: {lastIndex+1}")
        return lastIndex + 1


    def compress(self, chars: List[str]) -> int:
        write = 0  # Pointer for where to write the next characters
        i = 0  # Start of each new character group
        
        while i < len(chars):
            char = chars[i]
            count = 0  # Reset count for the new character group
            
            # Count occurrences of the current character
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            
            # Write the character to the array
            chars[write] = char
            print(chars)
            write += 1
            
            # If count > 1, write the count to the array as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        print(chars)
        # After processing all character groups, 'write' is the length of the compressed string
        return write

# Example usage
if __name__ == "__main__":
    sol = Solution()
    sol.compress(["a","a","b","b","c","c","c"])
    # print(sol.compress(["a","a","b","b","c","c","c"]))  # Output: 6 (["a","2","b","2","c","3"])
    # print(sol.compress(["a"]))  # Output: 1 (["a"])
    # print(sol.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))  # Output: 4 (["a","b","1","2"])


# if __name__ == "__main__":
#     sol = Solution() 
#     sol.compress_v2(['a', 'a', 'b', 'b', 'c', 'c', 'c'])
#     sol.compress_v2(["a",'a', 'a', "b","b","b","b","b","b","b","b","b","b","b","b"])
#     sol.compress_v2(["a", "b","b","b","b","b","b","b","b","b","b","b","b"])
#     sol.compress_v2(["a"]) 
#     sol.compress_v2(["a","a","a","b","b","a","a"])