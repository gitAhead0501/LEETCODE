"""
1007. Minimum Domino Rotations For Equal Row

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino. (A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)
We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.
Return the minimum number of rotations so that all the values in tops are the same, or all the values in bottoms are the same.
If it cannot be done, return -1.


Constraints:
A) 2 <= tops.length <= 2 * 10^4
B) bottoms.length == tops.length
C) 1 <= tops[i], bottoms[i] <= 6

Approach: Store the count of each value in tops and bottoms separately and also count the occurence in both at same time. Now run a loop from 1 to 6, and if the sum of occurences of a digit in tops and bottoms after removing the occurence in both equals the size of the tops/bottoms array then we can swap all digits in A or B. Count this occurence of minimum between tops and bottoms. If ans variable does not change then it is not possible to swap so return -1

"""

from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        ca = [0]*7
        cb = [0]*7
        cs = [0]*7
        for i in range(n):
            a,b = tops[i],bottoms[i]
            ca[a]+=1
            cb[b]+=1
            if a==b:
                cs[a]+=1
        ans = n
        for i in range(1,7):
            if ca[i]+cb[i]-cs[i]==n:
                minswap = min(ca[i],cb[i])-cs[i]
                ans = min(ans,minswap)
        return -1 if ans==n else ans
        



t1 = [2,1,2,4,2,2]
b1 = [5,2,6,2,3,2]
obj1 = Solution()
print(obj1.minDominoRotations(t1,b1))

obj2 = Solution()
t2 = [3,5,1,2,3]
b2 = [3,6,3,3,4]
print(obj2.minDominoRotations(t2,b2))