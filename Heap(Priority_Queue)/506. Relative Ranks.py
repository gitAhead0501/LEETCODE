"""
506. Relative Ranks
You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.


Constraints:
A) n == score.length
B) 1 <= n <= 104
C) 0 <= score[i] <= 106
D) All the values in score are unique.

Approach: Create a hashtable and store arr values, find the minimum value of score in heapq form of score and assign lenth of score to the popped value in hashtable and repeat this process, till length of score is 3: now assign "Bronze" to 3rd : "Silver" to 2nd : "Gold" to 1st

"""

import heapq
from typing import List


# 1)
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        h = {v:0 for v in score}
        heapq.heapify(score)
        for i in range(len(score)):
            ans = heapq.heappop(score)
            n = len(score)
            if n+1>3:
                h[ans] = str(n+1)
                n-=1
            else:
                if n==2:
                    h[ans] = "Bronze Medal"
                elif n==1:
                    h[ans] = "Silver Medal"
                else:
                    h[ans] = "Gold Medal"
                    break
        return h.values()



# 2) 
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        d, m = {}, []
        s = sorted(score, reverse = True)
        for i in range(len(s)):
            if i == 0:
                d[s[i]] = 'Gold Medal'
            elif i == 1:
                d[s[i]] = 'Silver Medal'
            elif i == 2:
                d[s[i]] = 'Bronze Medal'
            else:
                d[s[i]] = str(i+1)
        for i in score:
            m.append(d[i])
        return m