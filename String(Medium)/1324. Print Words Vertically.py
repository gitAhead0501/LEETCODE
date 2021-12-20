"""
1324. Print Words Vertically

Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.

Constraints:
A) 1 <= s.length <= 200
B) s contains only upper case English letters.
C) It's guaranteed that there is only one space between 2 words.

Approach: Zip each word in the list just like transposing a matrix : use ziplongest to fill the empty spaces

"""

from itertools import zip_longest
from typing import List

# 1)
class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split()
        for i in range(len(s)):
            s[i] = list(s[i])
        ls = list(zip_longest(*s,fillvalue=' '))
        for i in range(len(ls)):
            ls[i] = "".join(ls[i])
            ls[i] = ls[i].rstrip()
        return ls