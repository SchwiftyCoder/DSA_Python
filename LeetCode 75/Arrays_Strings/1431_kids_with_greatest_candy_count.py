"""
1431. Kids With the Greatest Number of Candies
Easy
Topics
Companies
Hint
There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

 

Example 1:

Input: candies = [2,3,5,1,3], extraCandies = 3
Output: [true,true,true,false,true] 
Explanation: If you give all extraCandies to:
- Kid 1, they will have 2 + 3 = 5 candies, which is the greatest among the kids.
- Kid 2, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
- Kid 3, they will have 5 + 3 = 8 candies, which is the greatest among the kids.
- Kid 4, they will have 1 + 3 = 4 candies, which is not the greatest among the kids.
- Kid 5, they will have 3 + 3 = 6 candies, which is the greatest among the kids.
Example 2:

Input: candies = [4,2,1,1,2], extraCandies = 1
Output: [true,false,false,false,false] 
Explanation: There is only 1 extra candy.
Kid 1 will always have the greatest number of candies, even if a different kid is given the extra candy.
Example 3:

Input: candies = [12,1,12], extraCandies = 10
Output: [true,false,true]
"""

from typing import List

class Solution:
    # O(n^2) solution
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        current solution runs in O(n^2) time due to the externa, for loop and the use of the max function.
        """
        result = []

        for i in range(len(candies)):
            # update kids candy count
            candies[i] += extraCandies
            # check if the increase is the greatest amongth the candie count
            is_max = max(candies) == candies[i]
            
            result.append(is_max if is_max else False)

            # revert to the original candy count
            candies[i] -= extraCandies

        return result


    # O(n) solution
    def kidsWithCandies_v2(self, candies: List[int], extraCandies: int) -> List[int]:
        # determine the kid with the highest candy count
        # this is crucial because it serves as a benchmark for comparing all other kids candy counts

        result = []
        highest_candy_count = max(candies)

        # check every other kids count increament against the highest candy count
        for kids_candy in candies:
            result.append(True if kids_candy + extraCandies > highest_candy_count else False)

        return result

    
if __name__ == "__main__":
    sol = Solution()
    print(sol.kidsWithCandies(candies = [2,3,5,1,3], extraCandies = 3))

    print(sol.kidsWithCandies_v2(candies = [2,3,5,1,3], extraCandies = 3))