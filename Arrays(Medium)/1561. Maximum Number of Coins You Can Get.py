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

Approach: Add only the 2nd largest value from the end of the list starting from len//3 index
Methods:
1) Deque container
2) One liner

"""

from collections import deque
from typing import List


# 1) deque : TC: O(nlogn) & SC: O(n)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        ans = 0
        piles.sort()
        dq = deque(piles)
        while dq:
            dq.pop()
            ans += dq.pop()
            dq.popleft()
        return ans



# 2) one liner : TC: O(nlogn) & SC: O(n)
class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        return sum(sorted(piles)[len(piles)//3::2])