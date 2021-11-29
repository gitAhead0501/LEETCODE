"""
1528. Shuffle String
Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.

Constraints:
A) s.length == indices.length == n
B) 1 <= n <= 100
C) s contains only lower-case English letters.
D) 0 <= indices[i] < n
E) All values of indices are unique (i.e. indices is a permutation of the integers from 0 to n - 1).

Approach1: zip/map the indices and array values, then sort them wrt indices and return the string
Approach2: create an empty list and store indices[i] with value of s[i]
"""

from typing import List

# 1)
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = list(s)
        Z = [b for a,b in sorted(zip(indices, t))]
        print(Z)
        return ''.join(Z)


# 2)
class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        res = ['']*n
        for i in range(n):
            res[indices[i]] = s[i]
        return "".join(res)