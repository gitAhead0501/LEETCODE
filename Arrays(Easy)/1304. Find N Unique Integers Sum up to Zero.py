"""
1304. Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.

Constraints:
A) 1 <= n <= 1000

Approach: If n is odd, add 0 and add +/- random distinct values : If even, add only +/- random distinct values

"""

from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        mid = n // 2
        if (n & 1):    # IF N IS ODD
            return [num for num in range(-mid, mid + 1)]
        else:
            return [num for num in range(-mid, mid + 1) if num != 0]


class Solution:
    def sumZero(self, n: int) -> List[int]:
        ans = []
        if n%2==1: ans.append(0)
        i=1
        while len(ans)<n:
            ans.append(i)
            ans.append(-i)
            i+=1
        return ans