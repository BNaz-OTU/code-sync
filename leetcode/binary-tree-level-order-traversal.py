# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        final = []
        queue = deque()

        queue.append(root)

        if (root is None):
            return []

        while len(queue) > 0:
            level = list(queue)
            innerList = []

            for nodeQ in level:
                queue.popleft()

                if (nodeQ):
                    if (nodeQ.left is not None):
                        queue.append(nodeQ.left)

                    if (nodeQ.right is not None):
                        queue.append(nodeQ.right)
                    
                    innerList.append(nodeQ.val)
            
            final.append(innerList)

        return final