"""
1557. Minimum Number of Vertices to Reach All Nodes

Given a directed acyclic graph, with n vertices numbered from 0 to n-1, and an array edges where edges[i] = [fromi, toi] represents a directed edge from node fromi to node toi.

Find the smallest set of vertices from which all nodes in the graph are reachable. It's guaranteed that a unique solution exists.

Notice that you can return the vertices in any order.

Constraints:
A) 2 <= n <= 10^5
B) 1 <= edges.length <= min(10^5, n * (n - 1) / 2)
C) edges[i].length == 2
D) 0 <= fromi, toi < n
E) All pairs (fromi, toi) are distinct.

Approach: Return a list of nodes whose indegree is 0
Method1: Set difference : set of range n and set of outdegree nodes
Method2: Creating an array and increment for outdegree nodes and returning nodes where value is 0 i.e. not incremented
"""

from typing import List


# 1)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return list(set(range(n)) - set(j for i,j in edges))



# 2)
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = [0]*n
        for _,v in edges: graph[v] += 1
        return [i for i,x in enumerate(graph) if x==0]
