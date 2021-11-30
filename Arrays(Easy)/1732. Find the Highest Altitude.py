"""
1732. Find the Highest Altitude
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

Constraints:
A) n == gain.length
B) 1 <= n <= 100
C) -100 <= gain[i] <= 100

Approach1: Find the max prefix sum upto each index in each iteration
Approach2: Store all the prefix sum in an array and return max value from it

"""

from typing import List

# 1)
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = 0
        for i in range(len(gain)):
            ans = sum(gain[:i+1])
            res = max(ans,res)
        return res

# 2) 
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = [0]
        for i in range(len(gain)):
            alt.append(sum(gain[:i+1]))
        return max(alt)