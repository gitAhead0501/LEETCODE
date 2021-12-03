"""
1550. Three Consecutive Odds
Given an integer array arr, return true if there are three consecutive odd numbers in the array. Otherwise, return false.

Constraints:

1 <= arr.length <= 1000
1 <= arr[i] <= 1000

Approach: Brute
Methods:
1) For loop
2) ONE LINER : using string func
3) ONE LINER : using zip func

"""

from typing import List


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        s = 0
        for i in range(len(arr)-2):
            if (arr[i])%2 and (arr[i+1])%2 and (arr[i+2])%2:
                return True
        return False


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return "111" in "".join([str(i%2) for i in arr])
 


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return any(1 & a & b & c for a, b, c in zip(arr, arr[1:], arr[2:]))