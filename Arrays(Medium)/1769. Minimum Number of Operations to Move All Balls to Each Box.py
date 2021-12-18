"""
1769. Minimum Number of Operations to Move All Balls to Each Box

You have n boxes. You are given a binary string boxes of length n, where boxes[i] is '0' if the ith box is empty, and '1' if it contains one ball.

In one operation, you can move one ball from a box to an adjacent box. Box i is adjacent to box j if abs(i - j) == 1. Note that after doing so, there may be more than one ball in some boxes.

Return an array answer of size n, where answer[i] is the minimum number of operations needed to move all the balls to the ith box.

Each answer[i] is calculated considering the initial state of the boxes.

Constraints:
A) n == boxes.length
B) 1 <= n <= 2000
C) boxes[i] is either '0' or '1'.

Approach1: Not efficient : For each index, check the left and right side : it is '1' then add the abs diff of current index and all index abs diff on both sides

"""
from typing import List


# 1) TC: O(n*(m+n)) : where m is the length left side of array at current index and n is the length of right side of array at current index : SC: 0(n)
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        ans = []
        for i in range(len(boxes)):
            res = 0
            for j in range(i):
                if boxes[j]=='1':
                    res += abs(j-i)
            for k in range(i+1,n):
                if boxes[k]=='1':
                    res += abs(k-i)
            ans.append(res)
        return ans