"""
1431. Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each candies[i] represents the number of candies the ith kid has, and an integer extraCandies, denoting the number of extra candies that you have.

Return a boolean array result of length n, where result[i] is true if, after giving the ith kid all the extraCandies, they will have the greatest number of candies among all the kids, or false otherwise.

Note that multiple kids can have the greatest number of candies.

Constraints:
A) n == candies.length
B) 2 <= n <= 100
C) 1 <= candies[i] <= 100
D) 1 <= extraCandies <= 50

Approach: return a list with value True if after giving extracandies the kid has greater no. of candies than the rest of kids in the original list else False

"""

from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [True if i+extraCandies >= max(candies) else False for i in candies]