"""
1640. Check Array Formation Through Concatenation

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

Constraints:
A) 1 <= pieces.length <= arr.length <= 100
B) sum(pieces[i].length) == arr.length
C) 1 <= pieces[i].length <= arr.length
D) 1 <= arr[i], pieces[i][j] <= 100
E) The integers in arr are distinct.
F) The integers in pieces are distinct (i.e., If we flatten pieces in a 1D array, all the integers in this array are distinct).

Approach: Use pieces[0] as key for hashtable : Now get values from table corresponding to array

"""

from typing import List


class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        h = {x[0]:x for x in pieces}
        res = []
        for each in arr:
            res += h.get(each,[])
        return res == arr