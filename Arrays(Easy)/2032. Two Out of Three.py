"""
2032. Two Out of Three
Given three integer arrays nums1, nums2, and nums3, return a distinct array containing all the values that are present in at least two out of the three arrays. You may return the values in any order.

Constraints:
A) 1 <= nums1.length, nums2.length, nums3.length <= 100
B) 1 <= nums1[i], nums2[j], nums3[k] <= 100

Approach1: Count elements whose occurence is greater than 1 in set of arrays
Approach2: ONE LINER : finding intersection between 3 sets and then their union

"""

from typing import List

# 1)
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        def helper(arr):
            for each in set(arr):
                if each not in self.h:
                    self.h[each] = 1
                else:
                    self.h[each] += 1
        self.h = {}
        helper(nums1)
        helper(nums2)
        helper(nums3)
        return [k for k,v in self.h.items() if v>1]


# 2)
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        return set(nums1) & set(nums2) | set(nums2) & set(nums3) | set(nums1) & set(nums3)