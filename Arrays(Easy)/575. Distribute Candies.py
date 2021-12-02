"""
575. Distribute Candies
Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor.

The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, and she wants to eat the maximum number of different types of candies while still following the doctor's advice.

Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.

Constraints:
A) n == candyType.length
B) 2 <= n <= 104
C) n is even.
D) -10^5 <= candyType[i] <= 10^5

Approach1: Brute Force : TLE EXPECTED : Brute is for counting unique values
Approach2: Using hashtable for counting
Approach3: ONE LINER : Counter

"""
from typing import List


# 1) BRUTE FORCE
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        uq = 0
        for i in range(len(candyType)):
            for j in range(0,i):
                if candyType[i] == candyType[j]:
                    break
            else:
                uq+=1
        return min(uq,len(candyType)//2)


# 2)
from collections import Counter
class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        return min(len(candyType) // 2, len(Counter(candyType)))