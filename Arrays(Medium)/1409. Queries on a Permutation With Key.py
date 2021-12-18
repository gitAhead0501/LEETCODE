"""
1409. Queries on a Permutation With Key

Given the array queries of positive integers between 1 and m, you have to process all queries[i] (from i=0 to i=queries.length-1) according to the following rules:

In the beginning, you have the permutation P=[1,2,3,...,m].
For the current i, find the position of queries[i] in the permutation P (indexing from 0) and then move this at the beginning of the permutation P. Notice that the position of queries[i] in P is the result for queries[i].
Return an array containing the result for the given queries.

Constraints:
A) 1 <= m <= 10^3
B) 1 <= queries.length <= m
C) 1 <= queries[i] <= m

Approach1: Make the p permutation list a deque container and make changes in it : remove value from p and appendleft value to it and return the desired array : Not Very Efficient

"""

from collections import deque
from typing import List


# 1)
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = list(range(1,m+1))
        p = deque(p)
        ans = []
        for x in queries:
            idx = p.index(x)
            ans.append(idx)
            p.remove(x)
            p.appendleft(x)
        return ans