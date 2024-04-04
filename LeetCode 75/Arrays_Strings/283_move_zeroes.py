"""
283. Move Zeroes 
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
"""

from typing import List
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        use 2 pointers:
            left = 0
            right = 0
        iterate though list using right
        if [right] != 0:
            swap with [left] and then
            increase left by 1

            NOTE: the reason for this swap is because we want to move all 0s to the right while non-zeroes to the left
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        print(nums)


    def moveZeroes_v2(self, nums: List[int]) -> None:
        """
        move all none zero elemenys to the left
        add zeroes to the arrray up to the length
        
        """
        write = 0
        for item in nums:
            if item != 0:
                nums[write] = item
                write += 1

        print(nums)

        # padd on any remaining 0s
        while write < len(nums):
            nums[write] = 0
            write += 1
        
        print(nums)
        


if __name__ == "__main__":
    sol = Solution()
    # sol.moveZeroes([0,1,0,3,12])
    sol.moveZeroes_v2([0,1,0,3,12])
    # sol.moveZeroes([1,0])
    # sol.moveZeroes([2,1])