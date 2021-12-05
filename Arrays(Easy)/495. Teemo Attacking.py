"""
495. Teemo Attacking
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

Constraints:
A) 1 <= timeSeries.length <= 10^4
B) 0 <= timeSeries[i], duration <= 10^7
C) timeSeries is sorted in non-decreasing order.

Approach: If difference of adjacent times is less than duration, then only add that difference : if it is greater than add the duration to the ans

"""

from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        for i in range(len(timeSeries)-1):
            if timeSeries[i+1]-timeSeries[i] > duration:
                total += duration
            else:
                total += timeSeries[i+1]-timeSeries[i]
        return total + duration



class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        t = 0
        for i in range(len(timeSeries)-1):
            t+= min(timeSeries[i+1]-timeSeries[i],duration)
        return t+duration