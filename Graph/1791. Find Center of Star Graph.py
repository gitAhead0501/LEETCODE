"""
1791. Find Center of Star Graph

There is an undirected star graph consisting of n nodes labeled from 1 to n. A star graph is a graph where there is one center node and exactly n - 1 edges that connect the center node with every other node.

You are given a 2D integer array edges where each edges[i] = [ui, vi] indicates that there is an edge between the nodes ui and vi. Return the center of the given star graph.

Constraints:
A) 3 <= n <= 105
B) edges.length == n - 1
C) edges[i].length == 2
D) 1 <= ui, vi <= n
E) ui != vi
F) The given edges represent a valid star graph.

Approach: Only need to compare first two edges, find the common cell in both
Method1: Hashtable for check common of each edges : TC : O(V+E)
Method2: Compare only first two edges TC: O(1)
Method3: Set Intersection

"""


from typing import List


# 1)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        h = {}
        for each in edges:
            for i in each:
                if i not in h:
                    h[i] = 1
                else:
                    h[i] += 1
        for k,v in h.items():
            if v>1:
                return k


# 2)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        if edges[0][0] in edges[1]:
            return edges[0][0]
        else:
            return edges[0][1]



# 3)
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        return (set(edges[0]) & set(edges[1])).pop()