"""
1441. Build an Array With Stack Operations

Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
Return the operations to build the target array. You are guaranteed that the answer is unique.

Constraints:
A) 1 <= target.length <= 100
B) 1 <= target[i] <= n
C) 1 <= n <= 100
D) target is strictly increasing.

Approach: Build array : if element is not present add 'Push' + 'Pop' else add only 'Push'

"""

from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        arr = []
        i = 1
        while i <= n and i <= target[-1]:
            if i not in target:
                arr.append("Push")
                arr.append("Pop")
            else:
                arr.append("Push")
            i += 1
        return arr