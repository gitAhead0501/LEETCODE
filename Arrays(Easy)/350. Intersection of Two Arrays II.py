"""
350. Intersection of Two Arrays II

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

Constraints:
A) 1 <= nums1.length, nums2.length <= 1000
B) 0 <= nums1[i], nums2[i] <= 1000

Approach1: Find interesction using counter or set but set does not returns duplicates so we use counter : ONE LINER
Methods: This can be written in one line or using for loops using Counter method or using hashtable

TC: O(n)

"""


from collections import Counter
from typing import List

# 1)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return (Counter(nums1) & Counter(nums2)).elements()



# 2)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a,b = Counter(nums1), Counter(nums2)
        res = []
        for k,v in b.items():
            if k in a:
                res += [k]*min(v, a[k])
        return res


# 3)
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h = {}
        for each in nums1:
            if each not in h:
                h[each] = 0
            h[each] += 1
        res = []
        for each in nums2:
            if each in h:
                if h[each] > 0:
                    res.append(each)
                    h[each] -= 1
        return res