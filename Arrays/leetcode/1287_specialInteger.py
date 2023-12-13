"""
1287. Element Appearing More Than 25% In Sorted Array

Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1
 
Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 105
"""

from typing import List
class Solution:

    def findSpecialInteger(self, arr: List[int]) -> int:
        # convert arr

        for element in arr:
            if element not in dict:
                dict[element] = 1
            else:
                dict[element] += 1

        # check which one has more than 25% occurence
        maxOccurence = [0, 0]
        for key, value in dict.items():
            if value > maxOccurence[0]:
                maxOccurence[0] = value
                maxOccurence[1] = key

        return maxOccurence[1]
    
sol = Solution()
print(sol.findSpecialInteger([1,1]))
print(sol.findSpecialInteger([1,2,2,6,6,6,6,7,10]))