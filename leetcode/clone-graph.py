"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# USED SOLN: https://www.youtube.com/watch?v=mQeF6bN8hMk
from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(root):
            if root in oldToNew:
                return oldToNew[root]
            
            copy = Node(root.val)
            oldToNew[root] = copy

            for nei in root.neighbors:
                copy.neighbors.append(dfs(nei))
            
            return copy

        if node is None:
            return None         
        
        return dfs(node)