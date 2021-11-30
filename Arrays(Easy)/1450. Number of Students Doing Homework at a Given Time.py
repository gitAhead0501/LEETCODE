"""
1450. Number of Students Doing Homework at a Given Time
Given two integer arrays startTime and endTime and given an integer queryTime.

The ith student started doing their homework at the time startTime[i] and finished it at time endTime[i].

Return the number of students doing their homework at time queryTime. More formally, return the number of students where queryTime lays in the interval [startTime[i], endTime[i]] inclusive.

Constraints:
A) startTime.length == endTime.length
B) 1 <= startTime.length <= 100
C) 1 <= startTime[i] <= endTime[i] <= 1000
D) 1 <= queryTime <= 1000

Approach: Just follow the problem statement

"""

from typing import List


class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0
        for i in range(len(startTime)):
            if endTime[i] >= queryTime and startTime[i] <= queryTime:
                count += 1
        return count