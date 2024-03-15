"""
88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:

Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:

Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1.
 

Constraints:

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-10^9 <= nums1[i], nums2[j] <= 109
"""
# type hints such as List[int]
from typing import List


class Solution:
    """
    Algorithmic analysis:
    Time complexity: O(m+n) since we loop through both elements
    Space Complexity: O(1) since we are only storing a value usig the pointers one at a time in the loop
    """
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        pointer1 = m - 1
        pointer2 = n - 1
        index = (m+n) - 1
        while pointer2 >= 0:
            if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
                nums1[index] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[index] = nums2[pointer2]
                pointer2 -= 1
            index -= 1
        
        # print the array nums1 when the method is called
        print(nums1)

    
    # method 2: a lazier approach
    # append all the elements from the second list into the first list and then perfom a sort operation on it
    # less efficient: runs in O(nlogn) time since it uses .sort() which implementsa time sort in python
    # space complexity: O(n) where n is the number of elements in the 
    def merge_v2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None: 
        mergeStart = m
        for item in nums2:
            nums1[mergeStart] = item
        nums1.sort()

        print(nums1)


# test cases
test_cases = Solution()
test_cases.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# test_cases.merge( nums1 = [1], m = 1, nums2 = [], n = 0)
# test_cases.merge( [1], 1, [], 0)
test_cases.merge([0], 0, [1], 1)
 
