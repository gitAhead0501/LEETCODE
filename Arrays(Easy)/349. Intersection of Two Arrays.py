"""
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Constraints:
A) 1 <= nums1.length, nums2.length <= 1000
B) 0 <= nums1[i], nums2[i] <= 1000

Approach1: Use set to determine the intersection of nums1 and nums2
Approach2: Use hashtable to store nums1 and check nums2

"""


from typing import List

# 1)
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


# 2) 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        for each in set(nums1):
            if each not in h:
                h[each] = 1
            else:
                h[each] += 1
        return [each for each in set(nums2) if each in h]