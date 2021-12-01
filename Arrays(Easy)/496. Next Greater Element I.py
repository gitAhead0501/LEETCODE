"""
496. Next Greater Element I
The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.

Constraints:
A) 1 <= nums1.length <= nums2.length <= 1000
B) 0 <= nums1[i], nums2[i] <= 10^4
C) All integers in nums1 and nums2 are unique.
D) All the integers of nums1 also appear in nums2.

Approach: Iterate from end of the array find greater element of each to the right of each num and put it in stack : stack top will be the greatest element to the right of each number : store these in hash table : and obtain values comparing with nums1

"""

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        h, stack = {}, []
        for each in nums2[::-1]:
            while stack and each > stack[-1]:
                stack.pop()
            if stack:
                h[each] = stack[-1]
            stack.append(each)
        return [h.get(num,-1) for num in nums1]