"""
Given an integer array nums, find the 
subarray with the largest sum, and return its sum.

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
"""

from typing import List


class Solution:
    """
    time complexity: O(n^2) where n is the number of elements in the array,
                    squared because for every nth element, we step through the array n times to the end of it
    """

    def maxSubArray(self, nums: List[int]) -> int:
        # set assume first element is overall max
        overallMax = nums[0]

        # step through the array elements
        for index in range(len(nums)):
            # set the next element to local sum
            currentMax = nums[index]
            if currentMax > overallMax:
                overallMax = currentMax
            # step through the rest of the array, ading up next neelement to local max and compare with overall max and swap if necessary
            for index2 in range(index + 1, len(nums)):
                # find a new current max and check with overall max, swap if necessary
                currentMax += nums[index2]
                if currentMax > overallMax:
                    overallMax = currentMax

        return overallMax

    """
    much more efficient because it runs in O(n) time
    the reason being that we find the local sum incrementally instead of iterating over the same elements to the end
    """

    def maxSubArray_v2(self, nums: List[int]) -> int:
        # set initial sum ot 0 and overall sum to first element
        currentSum = 0
        overallSum = nums[0]
        for number in nums:
            print(f"local sum: {currentSum}\nGlobal sum: {overallSum}\n")
            currentSum = max(number, (number + currentSum))
            overallSum = max(currentSum, overallSum)
            # currentSum = number if number > (number + currentSum) else (number + currentSum)
            # overallSum = currentSum if currentSum > overallSum else overallSum

        return overallSum


solution = Solution()
# print(solution.maxSubArray([5, 4, -1, 7, 8]))
# print(solution.maxSubArray([1]))
# print(solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))


print(solution.maxSubArray_v2([5, 4, -1, 7, 8]))
# print(solution.maxSubArray_v2([1]))
# print(solution.maxSubArray_v2([-2,1,-3,4,-1,2,1,-5,4]))
