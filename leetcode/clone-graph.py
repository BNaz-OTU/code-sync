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
        if (node is None):
            return None

        adjList = {}

        def dfs(node):
            print(node.val)
            adjList[node] = Node(node.val)

            for node_nei in node.neighbors:
                if (node_nei in adjList):
                    new_nei = adjList[node_nei]
                    adjList[node].neighbors.append(new_nei)
                else:
                    dfs(node_nei)
                    new_nei = adjList[node_nei]
                    adjList[node].neighbors.append(new_nei)

        
        dfs(node)

        return adjList[node]