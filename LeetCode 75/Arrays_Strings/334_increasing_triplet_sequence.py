"""
334. Increasing Triplet Subsequence 

Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
"""

from typing import List
class Solution:

    def increasingTriplet(self, nums: List[int]) -> bool:
        """
        Appraoch 1: runs in O(n^3) time, not very efficient
        """
        incTrip = []
        for i in range(len(nums)):
            incTrip.append(i)
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    incTrip.append(j)
                    for k in range(j+1, len(nums)):
                        if nums[k] > nums[j]:
                            incTrip.append(k)
                            return True
            incTrip = []
        return False
    
    def increasingTriplet_v2(self, nums: List[int]) -> bool:
        """
        Approach 2:
        iterate through the indexes i = 1 to i = len() - 2
        check if any left value is les and right value is greater
        """ 
        isLeftSmall, isRightBigger = False, False
        for j in range(1, len(nums) - 1):
            print(f"current element: {nums[j]}")
            # look for a left element that is smaller than element at index j
            for i in range(j-1, -1, -1):
                print(f"left element: {nums[i]}")
                print(f"is {nums[i]} < {nums[j]}: {nums[i] < nums[j]}")
                if nums[i] < nums[j]:
                    isLeftSmall = True 
                    break

            # look for a right element that is larger than element at j
            for k in range(j + 1, len(nums)):
                print(f"right element: {nums[k]}")
                print(f"is {nums[k]} > {nums[j]}: {nums[k] > nums[j]}")
                if nums[k] > nums[j]:
                    isRightBigger = True 
                    break

            if isLeftSmall and isRightBigger:
                print(f"{isLeftSmall}\n{isRightBigger}")
                return True
            
            # reset boolean values
            isLeftSmall, isRightBigger = False, False

        return False


    def increasingTriplet_v3(self, nums: List[int]):
        """
        Approach 3: 
        build two lists, leftMin and rightMax
        leftMin: minimum elements starting from th left
        rightMax: maximum elements starting from the right
        initialize with both elements at i = 0 and i = len(nums) - 1 

        runs in O(n) time
        """
        if len(nums) < 3:
            return False

        print(f"         :  {nums}")
        # Initialize leftMin and rightMax
        n = len(nums)
        leftMin = [0] * n
        rightMax = [0] * n
        
        leftMin[0] = nums[0]
        for i in range(1, n):
            leftMin[i] = min(leftMin[i-1], nums[i])
        
        rightMax[n-1] = nums[n-1]
        for i in range(n-2, -1, -1):
            rightMax[i] = max(rightMax[i+1], nums[i])

        rightMax = rightMax[::-1]
        print(f"left mins: {leftMin}\nright max: {rightMax}")

        for j in range(0, n):
            print(f"\nleft min: {leftMin[j]}\nmiddle: {nums[j]}\nright max: {rightMax[j]}")
            if leftMin[j] < nums[j] and nums[j] < rightMax[j]:
                print(f"\nnumbers are: {leftMin[j]} < {nums[j]} < {rightMax[j]}")
                return True
        
        return False
    
    def increasingTriplet_v4(self, nums: List[int]) -> bool:
        """
        1. use two variables, v1, v2 both set to positive infinity
        2. make a single pass through the array
        3. assign first smaller number to v1, 
        4. if num in nums is greater than v1 but smaller than v2, assign num to v2
        5. check if num in nums is greater than both v1 and v2, return True

        end of loop, return false
        """
    
        if len(nums) < 3:
            return False

        first, second = float('inf'), float('inf')
        for num in nums:
            if num <= first: 
                first = num
            elif num <= second:  
                second = num
            else: 
                return True

        return False
                    


if __name__ == "__main__":
    sol = Solution()

    # true
    print(sol.increasingTriplet_v4([2,1,5,0,4,6]))
    # true
    print(sol.increasingTriplet_v4([1, 2, 3, 4, 5, 6]))

    # false
    print(sol.increasingTriplet_v4([1, 2, 3, 4, 5][::-1]))    
    
    # true
    # print(sol.increasingTriplet([2,1,5,0,4,6]))

    # true
    print(sol.increasingTriplet_v4([1,2,2147483647]))

    # false
    print(sol.increasingTriplet_v4([6,7,1,2]))

    # false
    print(sol.increasingTriplet_v4([0,4,2,1,0,-1,-3])) 



