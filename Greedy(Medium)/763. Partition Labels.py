"""
763. Partition Labels

You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

Return a list of integers representing the size of these parts.

Constraints:
A) 1 <= s.length <= 500
B) s consists of lowercase English letters.

Approach: Create a function to find the starting and last index of each character(only once using hashtable) and store in hashtable. Iterate over the hashtable values iterator and check the min left and max right occurence of each character update the min and max left,right value(min idx and max idx). If next iterator has greater elements than all the previous stored values update left and right and before updating store the previous values in array. Now return the array of with values of right-left+1 i.e. the length of the substring required.

"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        def findFL(c):
            first,last = 0,0
            for i,x in enumerate(s):
                if x==c:
                    first = i
                    break
            for j in range(len(s)-1,-1,-1):
                if s[j]==c:
                    last = j
                    break
            return (first,last)
        h  = {}
        for x in s:
            if x not in h:
                h[x] = findFL(x)
        res = [each for each in h.values()]
        ls = []
        l,r = 0,0
        for x,y in res:
            if l>=x or r>=y or r>=x:
                l,r = min(l,r,x,y),max(l,r,x,y)
            else:
                ls.append((l,r))
                l,r = min(x,y),max(l,r,x,y)
        ls.append((l,r))
        ans = []
        for x,y in ls:
            ans.append(y-x+1)
        return ans