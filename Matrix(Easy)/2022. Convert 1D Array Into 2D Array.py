"""
2022. Convert 1D Array Into 2D Array

You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n. You are tasked with creating a 2-dimensional (2D) array with m rows and n columns using all the elements from original.

The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array, the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.

Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

Constraints:
A) 1 <= original.length <= 5 * 104
B) 1 <= original[i] <= 105
C) 1 <= m, n <= 4 * 104

Approach: Same as in reshaping of matrix : given an array form matrix from it
Methods: Using list slice

"""

from typing import List

# 1)
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m*n:
            return []
        ans = []
        for i in range(0,len(original),n):
            ans.append(original[i:i+n])
        return ans
    

# 2)
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        return [original[i*n:(i+1)*n] for i in range(m) if len(original)==m*n]