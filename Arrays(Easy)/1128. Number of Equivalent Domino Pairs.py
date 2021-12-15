"""
1128. Number of Equivalent Domino Pairs

Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if either (a == c and b == d), or (a == d and b == c) - that is, one domino can be rotated to be equal to another domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent to dominoes[j].

Constraints:
A) 1 <= dominoes.length <= 4 * 10^4
B) dominoes[i].length == 2
C) 1 <= dominoes[i][j] <= 9

Approach: Create a hashtable for each pair and set default value as 0 : then for each pair add its value to ans : add again for reverse of the pair : increment by 1 the value each pair in hashtable

"""

from collections import defaultdict
from typing import List

# 1)
class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        h = defaultdict(int)
        ans = 0
        for x,y in dominoes:
            ans += h[x,y]
            if x!=y: ans += h[y,x]
            h[x,y] += 1
        return ans