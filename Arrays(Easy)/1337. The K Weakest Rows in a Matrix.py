"""
1337. The K Weakest Rows in a Matrix
You are given an m x n binary matrix mat of 1's (representing soldiers) and 0's (representing civilians). The soldiers are positioned in front of the civilians. That is, all the 1's will appear to the left of all the 0's in each row.

A row i is weaker than a row j if one of the following is true:

The number of soldiers in row i is less than the number of soldiers in row j.
Both rows have the same number of soldiers and i < j.
Return the indices of the k weakest rows in the matrix ordered from weakest to strongest.

Constraints:
A) m == mat.length
B) n == mat[i].length
C) 2 <= n, m <= 100
D) 1 <= k <= m
E) matrix[i][j] is either 0 or 1.

Approach1: Count the number of soldiers using Binary Search and return rows sorted upto k length
Approach2: Store soldiers and their indices and return the order of weakest to strongest soldier's i.e. rows : upto k length [Least Efficient] 
Approach3: Do not count , just sort with sum of soldiers as they denote 1 and return 

"""

from collections import Counter
from typing import List

# 1) TIME COMPLEXITY : O(m*(logn+logm)) , SC : O(n)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            count = self.soldier_count(mat[i])
            res.append([count,i])
        res.sort()
        return [res[i][1] for i in range(k)]
    
    def soldier_count(self, row: List[int]) -> int:
        low, high = 0, len(row)
        while low < high:
            mid = low + (high-low)//2
            if row[mid]==1:
                low = mid + 1
            else:
                high = mid
        return low

# 2) TIME COMPLEXITY : O(n*m + nlogn) , SC : O(n)
from collections import Counter
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            cnt = Counter(mat[i])
            res.append([cnt[1],i])
        res.sort()
        return [res[i][1] for i in range(k)]


# 3) TIME COMPLEXITY : O(m*(n + logm)) , SC : O(n)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for i in range(len(mat)):
            res.append([sum(mat[i]),i])
        res.sort()
        return [res[i][1] for i in range(k)]
    
    # ONE LINER : return sorted(range(len(mat)), key=lambda x: sum(mat[x]))[:k]