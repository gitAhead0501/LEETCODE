"""
1817. Finding the Users Active Minutes

You are given the logs for users' actions on LeetCode, and an integer k. The logs are represented by a 2D integer array logs where each logs[i] = [IDi, timei] indicates that the user with IDi performed an action at the minute timei.

Multiple users can perform actions simultaneously, and a single user can perform multiple actions in the same minute.

The user active minutes (UAM) for a given user is defined as the number of unique minutes in which the user performed an action on LeetCode. A minute can only be counted once, even if multiple actions occur during it.

You are to calculate a 1-indexed array answer of size k such that, for each j (1 <= j <= k), answer[j] is the number of users whose UAM equals j.

Return the array answer as described above.

Constraints:
A) 1 <= logs.length <= 104
B) 0 <= IDi <= 109
C) 1 <= timei <= 105
D)k is in the range [The maximum UAM for a user, 105].

Approach: Create a hashtable and store unique values using set() : Now increment the index of len(values) in hashtable : Long Code(uses two for loops for hashtable unique values) and Short Code(single for loop)

"""

from typing import List


# 1)
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0]*k
        h = {}
        for x,y in logs:
            if x not in h:
                h[x] = [y]
            else:
                h[x] += [y]
        h1 = {}
        for v in h.values():
            if len(set(v)) not in h1:
                h1[len(set(v))] = 1
            else:
                h1[len(set(v))] += 1
        
        for i in range(1,k+1):
            if i in h1:
                res[i-1] = h1[i]
        return res

        # or instead of using last 2 for loops
        for v in h.values():
            if len(set(v)) <= k:
                res[len(set(v))-1] += 1



# 2)
class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        mp = {}
        for i, t in logs: 
            mp.setdefault(i, set()).add(t)
        ans = [0]*k
        for v in mp.values(): 
            if len(v) <= k: 
                ans[len(v)-1] += 1
        return ans