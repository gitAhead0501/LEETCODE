"""
455. Assign Cookies
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child i has a greed factor g[i], which is the minimum size of a cookie that the child will be content with; and each cookie j has a size s[j]. If s[j] >= g[i], we can assign the cookie j to the child i, and the child i will be content. Your goal is to maximize the number of your content children and output the maximum number.

Constraints:
A) 1 <= g.length <= 3 * 104
B) 0 <= s.length <= 3 * 104
C) 1 <= g[i], s[j] <= 231 - 1

Approach: Sort both the arrays: for each child check if he is satisfied until cookies do not meet requirements
Count only once

"""

from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        i,j = 0,0
        while i<len(s) and j<len(g):
            if s[i]>=g[j]:
                print(s[i],g[j])
                j+=1
            i+=1
        return j