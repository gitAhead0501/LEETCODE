"""
599. Minimum Index Sum of Two Lists

Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

Constraints:
A) 1 <= list1.length, list2.length <= 1000
B) 1 <= list1[i].length, list2[i].length <= 30
C) list1[i] and list2[i] consist of spaces ' ' and English letters.
D) All the stings of list1 are unique.
E) All the stings of list2 are unique.

Approach1: Store sum of indices and restaurant, find min in sum of indices and return an array of restaurants whose indices sum equals min 

"""

from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        a = {x:i for i,x in enumerate(list1)}
        res = []
        for i,x in enumerate(list2):
            if x in a:
                res.append([i+a[x],x])
        s = min(res)[0]
        return [each[1] for each in res if each[0]==s]