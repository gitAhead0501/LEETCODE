"""
605. Can Place Flowers
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

Constraints:
A) 1 <= flowerbed.length <= 2 * 104
B) flowerbed[i] is 0 or 1.
C) There are no two adjacent flowers in flowerbed.
D) 0 <= n <= flowerbed.length

Approach: Check for empty plots and in it's adjacent position if yes then plant a seed there i.e. make the value at thet index 1, else continue

"""

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i,count = 0,0
        while i<len(flowerbed):
            if not flowerbed[i] and (not i or not flowerbed[i-1]) and (i==len(flowerbed)-1 or not flowerbed[i+1]):
                flowerbed[i] = 1
                i += 1
                count += 1
            if count>=n:
                return True
            i+=1
        return False