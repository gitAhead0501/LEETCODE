"""
997. Find the Town Judge

In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Constraints:
A) 1 <= n <= 1000
B) 0 <= trust.length <= 104
C) trust[i].length == 2
D) All the pairs of trust are unique.
E) ai != bi
F) 1 <= ai, bi <= n

Approach: Create an array , increment 1 in that array at index b where 'someone' trusts b and decrement 1 for 'someone': return index where value in count equals n-1

"""

from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        count = [0]*(n+1)
        for a,b in trust:
            count[a-1] -= 1
            count[b-1] += 1
        for i,x in enumerate(count):
            if x == n-1:
                return i+1
        return -1