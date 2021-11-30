"""
813. Find Anagram Mappings
Given two lists A and B, and B is an anagram of A. B is an anagram of A means B is made by randomizing the order of the elements in A.

We want to find an index mapping P, from A to B. A mapping P[i] = j means the ith element in A appears in B at index j.
These lists A and B may contain duplicates. If there are multiple answers, output any of them.

Constraints:
A) A, B have equal lengths in range [1, 100].
B) A[i], B[i] are integers in range [0, 10^5].

Approach: Use hashtable to store B (as we have to search items of A in B efficiently) and return array of indices of B found in A

"""


from typing import List


class Solution(object):
    def anagramMappings(self, A: List[int], B:List[int]):
        h = {x:i for i,x in enumerate(B)}
        return [h[k] for k in A]
