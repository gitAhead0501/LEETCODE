"""
1260. Shift 2D Grid
Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

Constraints:
A) m == grid.length
B) n == grid[i].length
C) 1 <= m <= 50
D) 1 <= n <= 50
E) -1000 <= grid[i][j] <= 1000
F) 0 <= k <= 100

Approach1: Since shifting right will put the last k cells in grid on the first k cells, we start from the kth cells from last, the index of which is m * n - k % (m * n) : create an array and put elements into it

Approach2: Reverse the whole matrix : Reverse first k cells : Reverse remaining m*n-k cells
TIME COMPLEXITY OF BOTH IS : O(m*n)

"""

from typing import List

# 1)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        start = m * n - k % (m * n)
        ans = []
        for i in range(start, m * n + start):
            j = i % (m * n)
            r, c =  j // n, j % n
            if not (j -start) % n:
                ans.append([])
            ans[-1].append(grid[r][c]) 
        return ans


# 2)
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        def reverse(lo,hi):
            nonlocal cols
            while lo<hi:
                r,c= divmod(lo,cols)
                i,j = divmod(hi,cols)
                grid[r][c], grid[i][j] = grid[i][j], grid[r][c]
                lo+=1
                hi-=1
        rows = len(grid)
        cols = len(grid[0])
        k %= rows*cols
        reverse(0,rows*cols-1)
        reverse(0,k-1)
        reverse(k,rows*cols-1)
        return grid