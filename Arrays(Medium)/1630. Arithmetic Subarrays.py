"""
1630. Arithmetic Subarrays

A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between every two consecutive elements is the same. More formally, a sequence s is arithmetic if and only if s[i+1] - s[i] == s[1] - s[0] for all valid i.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic:

1, 1, 2, 5, 7
You are given an array of n integers, nums, and two arrays of m integers each, l and r, representing the m range queries, where the ith query is the range [l[i], r[i]]. All the arrays are 0-indexed.

Return a list of boolean elements answer, where answer[i] is true if the subarray nums[l[i]], nums[l[i]+1], ... , nums[r[i]] can be rearranged to form an arithmetic sequence, and false otherwise.


Constraints:
A) n == nums.length
B) m == l.length
C) m == r.length
D) 2 <= n <= 500
E) 1 <= m <= 500
F) 0 <= l[i] < r[i] < n
G) -105 <= nums[i] <= 105

Approach: Find common difference and check it's consistency in given subarrays
Methods:
1) Find common diff and check it's consistency in set(subarrays)
2) 

"""

from typing import List


# 1) TC: O(len(r)*nlogn)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        n = len(l)
        for i in range(n):
            sub = nums[l[i]:r[i]+1]
            sub.sort()
            d = sub[1]-sub[0]
            if all(d==sub[i+1]-sub[i] for i in range(len(sub)-1)):
                ans.append(True)
            else:
                ans.append(False)
        return ans



# 2) TC: O(len(r)*n)
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def isArthmetic(n):
            st = set(n)
            if len(st) != len(n): return len(st)==1
            mx, mn = max(n), min(n)
            if (mx-mn)%(len(n)-1) !=0 : return False
            step = (mx-mn)//(len(n)-1)
            for i in range(mn,mx,step):
                if i not in st:
                    return False
            return True
        return [isArthmetic(nums[start:stop+1]) for start,stop in zip(l,r)]