"""
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Constraints:
A) 1 <= s.length <= 105
B) s[i] is either 'I' or 'D'.

Approach: Create an additional array and check if s[i] is 'I' then add no.s in increasing order from 0 to n else add no.s in decreasing order from n to 0 : till the length of the s
AD-HOC
"""

from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low, high = 0, len(s)
        ans = []
        for x in s:
            if x == 'I':
                ans.append(low)
                low += 1
            else:
                ans.append(high)
                high -= 1

        return ans + [low]