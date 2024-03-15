"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

 

Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""
from typing import List

class Solution:

    # can be solved using list comprehension
    def rotate(self, nums: List[int], k:int) -> None:  
        for i in range(k): 
            temp = nums.pop()
            # print(f"last element: {temp}")
            # print(f"nums: {nums}")
            nums.insert(0, temp)
            # print(f"nums: {nums}\n")  

        print(nums)

    def rotate_v2(self, nums: List[int], k:int) -> None:
        pointer1 = 0
        pointer2 = len(nums)-k
        if pointer2 <= 0:
            pass
        else:
            while pointer2 < len(nums): 
                temp = nums[pointer1]
                nums[pointer1] = nums[pointer2]
                nums[pointer2] = temp
                pointer1 += 1
                pointer2 += 1
            
        # for odd numbers, the middle value does not get swapped since there is no pair
        # thus, we slice the first n elements before the middle value, last m elements before the last vale and then slice the middle value 
        if len(nums) % 2 != 0: #confirms our array has odd number of elements
            middleValue = int(len(nums)/2) 
            nums[:] = nums[:middleValue] + nums[middleValue+1:] + [nums[middleValue]]

        print(nums)

    """
        Rotate the elements of the array to the right by k steps.

        Parameters:
        nums (List[int]): The list of integers to be rotated.
        k (int): The number of steps to rotate the array.

        Returns:
        None: The method modifies the list in place and does not return anything.
        """
    def rotate_v3(self, nums:List[int], k:int):
        n = len(nums)
        k %= n # takes care of edge cases where k > len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        print(nums)




solution = Solution()

solution.rotate_v3([-1, -100, 3, 99], 2) 
# solution.rotate_v3([1,2,3,4,5,6,7], 3)
# solution.rotate_v3([1], 1)

# solution.rotate([-1,-100,3,99], k = 2)
# print()
# solution.rotate([1,2,3,4,5,6,7], k = 3)


# solution.rotate_v2([-1,-100,3,99], k = 2) 
# solution.rotate_v2([1,2,3,4,5,6,7], k = 3)
# solution.rotate_v2([-1], -2)
# solution.rotate([-1], 2)

