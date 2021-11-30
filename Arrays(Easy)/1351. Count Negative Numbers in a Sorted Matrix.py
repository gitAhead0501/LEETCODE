"""
1351. Count Negative Numbers in a Sorted Matrix
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.

Constraints:
A) m == grid.length
B) n == grid[i].length
C) 1 <= m, n <= 100
D) -100 <= grid[i][j] <= 100

Approach1: BRUTE FORCE : Run a nested for loop and check every item in the matrix if it is -ive or not
Approach2: For loop : O(n+m) Time Complexity : We iterate from last row and first column as it has the minimum value in any row and maximum value in any column i.e. we check if matrix[n-1][0] is -ive then all elements in the row will be -ive : then we move to upper row : if not -ive then we move to next/forward column : AND SO ON
Approach3: Binary Search : For each row in matrix, count the -ive numbers via BSEARCH

"""

from typing import List

# 1) BRUTE FORCE
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for i in range(len(grid)-1, -1,-1):
            for j in range(len(grid[0])-1,-1, -1):
                if grid[i][j]<0:
                    count +=1
        return(count)


# 2) 
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row=len(grid)
        cols=len(grid[0])
        count=0
        i=row-1
        j=0
        while i>=0 and j< cols:
            if grid[i][j]<0:
                count+=(cols-j)
                i-=1
            else:
                j+=1
        return count


# 3)
class Solution:
    def bsearch(self,row: List) -> int:
        start = 0
        end = len(row)
        while start<end:
            mid = start + (end-start)//2
            if row[mid] < 0:
                end = mid
            else:
                start = mid+1
        return len(row)-start

    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for each in grid:
            count += self.bsearch(each)
        return count