"""
1561. Maximum Number of Coins You Can Get

There are 3n piles of coins of varying size, you and your friends will take piles of coins as follows:

In each step, you will choose any 3 piles of coins (not necessarily consecutive).
Of your choice, Alice will pick the pile with the maximum number of coins.
You will pick the next pile with the maximum number of coins.
Your friend Bob will pick the last pile.
Repeat until there are no more piles of coins.
Given an array of integers piles where piles[i] is the number of coins in the ith pile.

Return the maximum number of coins that you can have.

Constraints:
A) 3 <= piles.length <= 105
B) piles.length % 3 == 0
C) 1 <= piles[i] <= 104

Approach: Sort the array and sum all the 2nd index values from backward till no. of possible answers are available i.e. len(piles)//3

"""

from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        k = len(piles)//3
        i = len(piles)-1
        j = 0
        while i>0 and j<k:
            res += piles[i-1]
            i-=2
            j+=1
        return res

# one liner:
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles)//3::2])