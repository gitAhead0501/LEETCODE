"""
1331. Rank Transform of an Array
Given an array of integers arr, replace each element with its rank.

The rank represents how large the element is. The rank has the following rules:

Rank is an integer starting from 1.
The larger the element, the larger the rank. If two elements are equal, their rank must be the same.
Rank should be as small as possible.
 
Constraints:
A) 0 <= arr.length <= 10^5
B) -10^9 <= arr[i] <= 10^9

Approach: create a hashtable for storing ranks from 1 to len of arr : return a array of ranks getting value from arr
Methods: hash table or enumeration or map

"""

from typing import List

# 1)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        h = {val:idx+1 for idx,val in enumerate(sorted(set(arr)))}
        ans = []
        for each in arr:
            ans.append(h.get(each))
        return ans


# 2)
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        h = {val:idx+1 for idx,val in enumerate(sorted(set(arr)))}
        return map(h.get, arr)


# ONE LINER: 
# return map({val:idx+1 for idx,val in enumerate(sorted(set(arr)))},arr)