"""
1605. Find Valid Matrix Given Row and Column Sums

You are given two arrays rowSum and colSum of non-negative integers where rowSum[i] is the sum of the elements in the ith row and colSum[j] is the sum of the elements of the jth column of a 2D matrix. In other words, you do not know the elements of the matrix, but you do know the sums of each row and column.

Find any matrix of non-negative integers of size rowSum.length x colSum.length that satisfies the rowSum and colSum requirements.

Return a 2D array representing any matrix that fulfills the requirements. It's guaranteed that at least one matrix that fulfills the requirements exists.

Constraints:
A) 1 <= rowSum.length, colSum.length <= 500
B) 0 <= rowSum[i], colSum[i] <= 108
C) sum(rows) == sum(columns)

Approach: Greedily take the minimum of rowsum and colsum index by index and place it in the grid and change(decrement) the rowSum and colSum indices accordingly.

"""

from typing import List


class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m,n = len(colSum), len(rowSum)
        A = [[0]*m for _ in range(n)]
        i,j = 0,0
        while i<n and j<m:
            A[i][j] = min(rowSum[i],colSum[j])
            rowSum[i] -= A[i][j]
            colSum[j] -= A[i][j]
            if rowSum[i]==0:
                i+=1
            if colSum[j]==0:
                j+=1
        return A