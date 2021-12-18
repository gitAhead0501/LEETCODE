"""
2079. Watering Plants

You want to water n plants in your garden with a watering can. The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the ith plant is located at x = i. There is a river at x = -1 that you can refill your watering can at.

Each plant needs a specific amount of water. You will water the plants in the following way:

Water the plants in order from left to right.
After watering the current plant, if you do not have enough water to completely water the next plant, return to the river to fully refill the watering can.
You cannot refill the watering can early.
You are initially at the river (i.e., x = -1). It takes one step to move one unit on the x-axis.

Given a 0-indexed integer array plants of n integers, where plants[i] is the amount of water the ith plant needs, and an integer capacity representing the watering can capacity, return the number of steps needed to water all the plants.


Constraints:
A) n == plants.length
B) 1 <= n <= 1000
C) 1 <= plants[i] <= 106
D) max(plants[i]) <= capacity <= 109

Approach: If capacity is less than amount of water plants needs, go back to river i.e. add index i and i+1(to come back) and water again : repeat this process

"""

from typing import List


# 1) TC: O(n)
class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        cap = capacity
        step = 0
        for i,x in enumerate(plants):
            if capacity >= x:
                step += 1
                capacity -= x
            else:
                step += i
                step += i+1
                capacity = cap-x
        return step