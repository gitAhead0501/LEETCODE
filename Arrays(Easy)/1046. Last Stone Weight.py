"""
1046. Last Stone Weight

You are given an array of integers stones where stones[i] is the weight of the ith stone.

We are playing a game with the stones. On each turn, we choose the heaviest two stones and smash them together. Suppose the heaviest two stones have weights x and y with x <= y. The result of this smash is:

If x == y, both stones are destroyed, and
If x != y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
At the end of the game, there is at most one stone left.

Return the smallest possible weight of the left stone. If there are no stones left, return 0.

Constraints:
A) 1 <= stones.length <= 30
B) 1 <= stones[i] <= 1000

Approach: Pop first two elements from the sorted stones repeatedly until len of stones is 0 or 1 : return the weight of the smallest element i.e. reamining element in the stones

Methods: Using heap | Using Binary insort

"""

from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort(reverse = True)
        i = len(stones)
        while i>1:
            a = stones.pop(0)
            b = stones.pop(0)
            net = a-b
            if net:
                stones.append(net)
            stones.sort(reverse = True)
            i = len(stones)
        return stones[-1] if stones else 0