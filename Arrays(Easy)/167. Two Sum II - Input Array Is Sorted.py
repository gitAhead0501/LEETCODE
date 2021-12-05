"""
167. Two Sum II - Input Array Is Sorted
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

Constraints:
A) 2 <= numbers.length <= 3 * 10^4
B) -1000 <= numbers[i] <= 1000
C) numbers is sorted in non-decreasing order.
D) -1000 <= target <= 1000
E) The tests are generated such that there is exactly one solution.

Approach: create a hashtable and store target - nums val and return when nums appears in table

"""

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        h = {}
        for i,j in enumerate(numbers):
            k = target-j
            if k not in h:
                h[j] = i+1
            else:
                return [h[k],i+1]