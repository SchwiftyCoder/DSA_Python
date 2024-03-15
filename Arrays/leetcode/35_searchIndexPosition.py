"""
35. Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2: 
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""

from typing import List
class Solution:

    # solution runs in O(n) time complexity.
    def searchInsert(self, nums: List[int], target:int) -> int:   
        # return the index if the target is found
        for index in range(len(nums)): 
            # either the current element is the target or greatr than it
            if nums[index] >= target:   
                return index
            
            # return the index where it would be if inserted in order
            # if nums[index] > target:
            #     return index
            
        # return the index where it would be if inserted in order
        # for index in range(len(nums)):
        #     if nums[index] > target:
        #         return index
        

        # index must be at the end
        return len(nums)
    

    # solution two runs in O(log n) time complexity because it uses binary search
    def searchInsert_v2(self, nums:List[int], target:int) -> int:
        left, right = 0, len(nums) - 1
        # loop as long as left does not exceed right
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target: # target must be to the left: just before mid
                right = mid - 1
            else: # implies nums[mid] < target: target must be towards the right, just after mid
                left = mid + 1
        
        return left # last index after mid

solution = Solution() 
print(solution.searchInsert([1, 3, 5, 6], 5)) # returns 2
print(solution.searchInsert([1, 3, 5, 6], 2)) # returns 1
print(solution.searchInsert([1, 3, 5, 6], 7)) # returns 4
print(solution.searchInsert([1], 5))  # returns 1
print(solution.searchInsert([1], 0))  # returns 0

print()

print(solution.searchInsert_v2([1, 3, 5, 6], 5)) # returns 2
print(solution.searchInsert_v2([1, 3, 5, 6], 2)) # returns 1
print(solution.searchInsert_v2([1, 3, 5, 6], 7)) # returns 4
print(solution.searchInsert_v2([1], 5))  # returns 1
print(solution.searchInsert_v2([1], 0))  # returns 0


