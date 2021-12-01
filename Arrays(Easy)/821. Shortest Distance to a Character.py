"""
821. Shortest Distance to a Character

Given a string s and a character c that occurs in s, return an array of integers answer where answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.

The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Constraints:
A) 1 <= s.length <= 104
B) s[i] and c are lowercase English letters.
C) It is guaranteed that c occurs at least once in s.

Approach1: Brute force : TIME COMPLEXITY : O(n^2)
Approach2: TIME COMPLEXITY : O(n) and SPACE : O(n) : Calculate distances from left to right and right to left : return its min

"""
import math
from typing import List

# 1) TC : O(n^2)
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        c_pos = [i for i in range(len(s)) if s[i]==c]
        return [min(abs(i-c) for c in c_pos) for i in range(len(s))]


# 2) TC : O(n)
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        ans = []
        prev = -math.inf
        for i,x in enumerate(s):
            if x==c:
                prev = i
            ans.append(i-prev)
        prev = math.inf
        for i in range(len(s)-1,-1,-1):
            if s[i] == c:
                prev = i
            ans[i] = min(ans[i],prev-i)
        return ans