"""
169. Majority Element
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Constraints:
A) n == nums.length
B) 1 <= n <= 5 * 10^4
C) -2^31 <= nums[i] <= 2^31 - 1

Approach1: BRUTE FORCE : Count the frequencies of each in element in for loop itself and compare with len(nums)//2
Approach2: Since the majority elements appears more than n//2 times, the ans should be the middle element in the sorted array
Approach3: Using hashtable and then finding max value of a key in that and return that key
Approach4: Approach3 : 2 Lines
Approach5: Randomization : Because more than n//2 array indices are occupied by the majority element, a random array index is likely to contain the majority element : check repeatedly
Approach6: Boyer Moore Algorithm (to be learnt)
Approach7: Divide and Conquer (to be learnt)

"""

import random
from collections import Counter
from typing import List

# 1) BRUTE FORCE: TC : O(n^2) , SC : O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num


# 2) Short code : TC: O(nlogn) , SC: O(n) or O(1) : if modifying is not allowed then O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]


# 3) Hash Table : TC: O(n) , SC: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h = {}
        for each in nums:
            if each not in h:
                h[each] = 1
            else:
                h[each] += 1
        n = len(nums)//2
        for k,v in h.items():
            if v>n:
                return k

# 4) Counter : TC: O(n) , SC: O(n)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)
        return max(counts.keys(), key=counts.get)


# 5) Randomization : TC : O(n) , SC: O(1)
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate