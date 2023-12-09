"""
136. Single Number 

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.
"""

from typing import List
class Solution:


    def singleNumber(self, nums: List[int]) -> int:
        # use a dictionary to keep trakc of each element and their successive counts
        occurrence = {}
        for item in nums:
            if item not in occurrence:
                occurrence[item] = 1
            else:
                occurrence[item] += 1

        element = 0
        for key, value in occurrence.items():
            if value == 1:
                element = key
                break
            
        return element
    
    """
    Initialization of result: result is set to 0. In binary, 0 is neutral for XOR operations.

Iterating Over the List: The method iterates over each number in the nums list.

XOR Operation: For each number num in the list, result is updated to result ^ num. The XOR operation has the following properties:

If you XOR a number with itself, the result is 0 (e.g., a ^ a = 0).
If you XOR a number with 0, the result is the number itself (e.g., a ^ 0 = a).
XOR is commutative and associative, meaning a ^ b ^ a is the same as a ^ a ^ b, which equals b.
Finding the Unique Number: Since every number except one appears exactly twice, all paired numbers will cancel each other out (become 0). The only number that remains is the unique number that appears once.

Return Result: The final value of result after the loop is the single non-repeated number, which is returned by the method.
    """
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for num in nums:
            number ^= num

        return number

solutoin = Solution()
solutoin.singleNumber([2, 2, 1])
solutoin.singleNumber([4, 1, 2, 1, 2])