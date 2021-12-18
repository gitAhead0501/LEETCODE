"""
1282. Group the People Given the Group Size They Belong To

There are n people that are split into some unknown number of groups. Each person is labeled with a unique ID from 0 to n - 1.

You are given an integer array groupSizes, where groupSizes[i] is the size of the group that person i is in. For example, if groupSizes[1] = 3, then person 1 must be in a group of size 3.

Return a list of groups such that each person i is in a group of size groupSizes[i].

Each person should appear in exactly one group, and every person must be in a group. If there are multiple answers, return any of them. It is guaranteed that there will be at least one valid solution for the given input.

Constraints:
A) groupSizes.length == n
B) 1 <= n <= 500
C) 1 <= groupSizes[i] <= n

Approach: Create a hashtable and an array, only make a list of group size limit and append other values to other list : Efficient

"""

from typing import List


# 1) TC: O(m*n) : where m is the size of hashtable and n is the size of len of each value in hashtable
class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        h = {}
        for i,x in enumerate(groupSizes):
            if x not in h:
                h[x] = [i]
            else:
                h[x] += [i]
        ans = []
        for k,v in h.items():
            j = 0
            while j<len(v):
                ans.append(v[j:j+k])
                j+=k
        return ans