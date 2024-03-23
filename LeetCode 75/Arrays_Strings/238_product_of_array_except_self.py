"""
238. Product of Array Except Self 
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

"""

from typing import List
from functools import reduce

class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Approach:
            use two list to compute the pre/post fix product 
            list1: deafault initial value of 1
            list2: default initial value of 1 but at the end
        """
        prefix = [1] # append a 1 to the beginning 
        postfix = [1] # prepend a 1 to the end

        # 1 here is the multiplicative product

        pre = 1
        post = 1
        for i in range(len(nums)):
            pre *= nums[i] # multiply from the front
            post *= nums[-i-1] # multiply from the rear

            if len(prefix) != len(nums):
                prefix.append(pre)
            if len(postfix) != len(nums):
                postfix.append(post) # better 
                # postfix.insert(0, post) # still uses a for loop, yields a O(n^2)

        # reverse the postfix operation
        postfix = postfix[::-1]
        print(f"nums: {nums}\npre:  {prefix}\npost: {postfix}")
        # result = [prefix[i] * postfix[i] for i in range(len(nums))]
        result1 = [i * j for i, j in zip(prefix, postfix)]
        print(f"product except self: {result1}")



if __name__ == "__main__":
    sol = Solution()
    # sol.productExceptSelf([-1,1,0,-3,3])
    # sol.productExceptSelf([0,0]) 
    # sol.productExceptSelf([0,4,0])
    sol.productExceptSelf([1,2,3,4])