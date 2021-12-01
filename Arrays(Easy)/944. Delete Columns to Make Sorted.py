"""
944. Delete Columns to Make Sorted

You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

abc
bce
cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

Constraints:
A) n == strs.length
B) 1 <= n <= 100
C) 1 <= strs[i].length <= 1000
D) strs[i] consists of lowercase English letters.

Approach: Count the columns which are not equal to their sorted sequence : Can be One liner [Little more efficient than 4-5 lines of code]

"""

from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        strs = list(zip(*strs))
        count = 0
        for each in strs:
            if list(each) != sorted("".join(each)):
                count += 1
        return count
    # ONE LINER 
    # return sum(list(col)!= sorted(col) for col in zip(*strs))