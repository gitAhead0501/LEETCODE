"""
134. Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

Constraints:
A) gas.length == n
B) cost.length == n
C) 1 <= n <= 105
D) 0 <= gas[i], cost[i] <= 104

Approach: add gas[i]-cost[i] to the prev gastank value if -ive reset to 0 and start from next station and set it ans which maybe the orginial answer to the question
Methods: Also u can return the sum of gas< the sum of cost if it is not possible for any combo

"""

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        res,total = 0,0
        gastank = 0
        for i in range(len(gas)):
            gastank += gas[i]-cost[i]
            if gastank<0:
                res = i+1
                total += gastank
                gastank = 0
        total += gastank
        return -1 if total < 0 else res