"""
We have n chips, where the position of the ith chip is position[i].

We need to move all the chips to the same position. In one step, we can change the position of the ith chip from position[i] to:

position[i] + 2 or position[i] - 2 with cost = 0.
position[i] + 1 or position[i] - 1 with cost = 1.
Return the minimum cost needed to move all the chips to the same position.

Constraints:
A) 1 <= position.length <= 100
B) 1 <= position[i] <= 10^9

Approach: Move all the even positions to 0 in cost:0 and all odd positions to 1 in cost1: then return the min of coins on position 0 and 1

"""

from collections import Counter
from typing import List


class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        cnt = Counter(position)
        if 0 not in cnt:
            cnt[0] = 0
        if 1 not in cnt:
            cnt[1] = 0
        for k,v in cnt.items():
            if not k%2 and k!=0:
                cnt[0] += v
                cnt[k] = 0
            elif k%2 and k!=1:
                cnt[1] += v
                cnt[k] = 0
        return min(cnt[0],cnt[1])