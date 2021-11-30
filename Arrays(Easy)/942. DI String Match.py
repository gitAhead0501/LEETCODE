"""
942. DI String Match
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:

s[i] == 'I' if perm[i] < perm[i + 1], and
s[i] == 'D' if perm[i] > perm[i + 1].
Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.

Constraints:
A) 1 <= s.length <= 10^5
B) s[i] is either 'I' or 'D'.

Approach: We need to store numbers in co-ordination with given string, set according to them low and high

"""

from typing import List


class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        low,high = 0,len(s)
        ans = []
        for each in s:
            if each == 'I':
                ans.append(low)
                low+=1
            else:
                ans.append(high)
                high-=1
        return ans