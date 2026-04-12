"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        adjList = {}

        def dfs(node):
            if (node in adjList):
                return adjList[node]
            
            copyVal = Node(node.val)
            adjList[node] = copyVal

            for nei in node.neighbors:
                copyVal.neighbors.append(dfs(nei))
            
            return copyVal
        
        if node is None:
            return None
            
        return dfs(node)