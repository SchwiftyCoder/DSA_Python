"""

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
Custom Judge:

The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:

Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""

from typing import List  # used for type hints in python 3


class Solution:

    """
    this approach is wrong as it
    """

    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        # remove all duplicates
        for right in range(1, len(nums)):
            if nums[right] == nums[left]:
                nums[right] = "_"
            else:
                left = right

        print(f"nums with no dupes: \n{nums}")

        # move all underscores to end of array
        # one pointer at 1 since we are guranteed an element at index 0
        nonNone = 0
        for right in range(len(nums)):
            # print(f"left({left}): {nums[left]}\nright({right}): {nums[right]}\nnums: {nums}\n")
            if nums[right] != "_":
                nums[nonNone], nums[right] = nums[right], nums[nonNone]
                nonNone += 1

        print(f"nums with 'None' pushed to rght: \n{nums}\nleft: {nonNone}\n\n")
        print(f"nums memory location after processing elements: \n{id(nums)}")
        return nonNone

    def removeDuplicates_v2(self, nums: List[int]) -> int:
        if not nums:
            return 0

        left = 0

        for right in range(1, len(nums)):
            if nums[right] != nums[left]:
                left += 1
                nums[left] = nums[right]
            print(
                f"left ({left}) -> {nums[left]}\nright ({right}) -> {nums[right]}\nnums: {nums}\n\n"
            )

        return left + 1


solution = Solution()
nums = [0, 0, 0, 1, 1, 2, 2, 3, 3, 3, 3, 3, 3]
# print(f"nums memory location: {id(nums)}\n\n")
solution.removeDuplicates_v2(nums)
# print(f"nums memory location: {id(nums)}\n\n")
# solution.removeDuplicates([1,1,2])
# solution.removeDuplicates([1,1,2,2, 2, 4,4])
# solution.removeDuplicates([-1, 0, 1,1, 1, 2, 3, 3, 4, 5])
# solution.removeDuplicates([1,2])
