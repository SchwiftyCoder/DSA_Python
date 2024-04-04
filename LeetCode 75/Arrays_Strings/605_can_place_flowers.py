"""
605. Can Place Flowers
Easy
Topics
Companies
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
"""

from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        """
        go through each plot on the flowerbed
        if plot is 0
            if left and right plots == 0
            edge cases:
                0th index: check only right plot
                n-1 index: check only left plot
            eleminate edge cases:
                prepend and append a 0 to the flowerbed
                this way, we can always calculate the left and right adjacent plots 
            then decrease n by 1
            mark the spot in the array
        if n <= 0
            return True

        return False
                
        """ 
        flowerbed.insert(0, 0)
        flowerbed.append(0)
        for plot in range(1, len(flowerbed)-1):  
            # print(f"plot#: {plot-1}")
            left_plot = plot - 1 
            right_plot = plot + 1
            valid_adjacent_plot = flowerbed[left_plot] == 0 and flowerbed[right_plot] == 0
            if flowerbed[plot] == 0 and valid_adjacent_plot: 
                # print(f"left plot: {flowerbed[left_plot]} | md_plot: {flowerbed[plot]} | right plot: {flowerbed[right_plot]}")
                flowerbed[plot] = 1
                n -= 1
            if n <= 0:
                return True

        return False
    

    def canPlaceFlowers_v2(self, flowerbed: List[int], n: int) -> bool:
        """
        using sliding window technique 
            step through the array 3 elements at a time
            start: 0
            end = start + 2
            find the sum of arr[start:end+1]
            if sum == 0, 
                decrease n by 1
                update flowerbed plot content
            if n is less/equal to 0
            return true

            return false
        """ 
        for start in range(len(flowerbed)-2):
            end = start + 2;
            if sum(flowerbed[start:end+1]) == 0:
                n -= 1
                flowerbed[start+1] = 1
            if n <= 0:
                return True
            
        return False


sol = Solution()

# false
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 2))
print(sol.canPlaceFlowers_v2(flowerbed = [1,0,0,0,1], n = 2))
print()

# # false
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,0,1], n = 2))
print(sol.canPlaceFlowers_v2(flowerbed = [1,0,0,0,0,1], n = 2))
print()

# # true
print(sol.canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1))
print(sol.canPlaceFlowers_v2(flowerbed = [1,0,0,0,1], n = 1))
print()

# # true
print(sol.canPlaceFlowers(flowerbed = [0,0,0,0,0,1,0,0], n = 0))
print(sol.canPlaceFlowers_v2(flowerbed = [0,0,0,0,0,1,0,0], n = 0))
