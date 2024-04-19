"""
The Problem Statement
You are provided with a string that's a blend of alphabetic and non-alphabetic characters. Think of a beach where you find both shells (a-Z) and other things like plastic wrappers or dollar bills ($, !, etc.). For example, you might get:

TEXT
'sea!$hells3'
Your mission, should you choose to accept it, is to flip only the alphabetical shells while keeping the other items ($, !, etc.) in their original positions.

For example, when calling:

TEXT
reverseOnlyAlphabetical('sea!$hells3');
You should expect the output to be:

TEXT
'sll!$ehaes3'
Constraints to Consider
String Length: The length of the given string is up to 100,000 characters.
Character Set: You'll be working with ASCII characters.
Time Complexity: Aim for a time complexity of O(n).
Space Complexity: Aim for a space complexity of O(n).
"""

from typing import List, Optional

class Solution:

    def reverse_only_alpha(self, s: Optional[str]) -> Optional[str]:
        """
        convert string to list
        use two pointers, 
        l = 0
        r = len(s)-1
        loop as long as r > l
        if both [l] and [r] are letters
            swap them
            increase both l and r
        if only [l]
            increase l
        if only [r]
            decrease r

        return ''.join(list)

        """
        
        s_to_list: List = list(s)
        left: int = 0
        right: int = len(s)-1
        while right > left:
        # both left and right are alphabets, swap and increase both
            if s_to_list[left].isalpha() and s_to_list[right].isalpha():
                s_to_list[left], s_to_list[right] = s_to_list[right], s_to_list[left]
                left += 1
                right -= 1 
            # left is not alphabet, advance rightward
            elif not s_to_list[left].isalpha():
                left += 1
            # right is not an alphabet, advance leftward
            elif not s_to_list[right].isalpha():
                right -= 1
            
        new_s = ''.join(s_to_list)
            
        return new_s


if __name__ == "__main__":
    sol = Solution()
    # reverse_only_alpha('sea!$hells3') to return 'sll!$ehaes3'
    # reverse_only_alpha('1kas90jda3') to return '1adj90sak3'  
    print(sol.reverse_only_alpha('sea!$hells3'))
    print(sol.reverse_only_alpha('1kas90jda3'))