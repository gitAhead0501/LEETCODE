"""
1636. Sort Array by Increasing Frequency
Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.

Return the sorted array.

Constraints:
A) 1 <= nums.length <= 100
B)-100 <= nums[i] <= 100

Approach1: Count the frequency of each element and sort wrt frequencies : if freq is same sort in descending order : i.e. if a>b with same freq c then sort as b,a coz -b>-a 

Approach2: Sort the array in reverse, and then sort with key as count of each element : duplicate frequencies will remain unchanged i.e. in descending order and that is what we want
"""
from collections import Counter
from typing import List

# 1)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        cnt = Counter(nums)
        return sorted(nums, key=lambda x:(cnt[x],-x))


# 2)
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        return sorted(sorted(nums,reverse=1),key=nums.count)