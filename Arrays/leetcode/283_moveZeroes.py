"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        size = len(nums)
        for right in range(size):
            # print(f"left: {left}, right: {right}\nnums: {nums}\n")
            # only swap if left is 0
            if nums[right]: # same as nums[rihgt] != 0
                # print(f"if block: nums[left] == 0 and nums[right] != 0 i.e. {nums[right]}")
                nums[left], nums[right] = nums[right], nums[left]
                left += 1

        print(f"{nums}\n")

    def moveZeroes_v2(self, nums: List[int]):
        left = 0
        right = 0
        while right < len(nums):
            if nums[right] != 0:
                temp = nums[right]
                nums[right] = nums[left]
                nums[left] = temp
                left += 1
            right += 1
        print(nums)


solution = Solution()
solution.moveZeroes([0, 1])
solution.moveZeroes_v2([0, 1])
solution.moveZeroes([0, 1, 0, 3, 12])
solution.moveZeroes_v2([0, 1, 0, 3, 12])
solution.moveZeroes([0, 0, 0, 1, 2])
solution.moveZeroes_v2([0, 0, 0, 1, 2])
solution.moveZeroes([0, 0, 1])
solution.moveZeroes_v2([0, 0, 1])
solution.moveZeroes([1, 0])
solution.moveZeroes_v2([1, 0])
solution.moveZeroes([1, 0, 1])
solution.moveZeroes_v2([1, 0, 1])
solution.moveZeroes([4, 2, 4, 0, 0, 3, 0, 5, 1, 0])
solution.moveZeroes_v2([4, 2, 4, 0, 0, 3, 0, 5, 1, 0])
