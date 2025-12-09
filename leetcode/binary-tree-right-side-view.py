# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

# USED FOR REFERENCE: https://www.youtube.com/watch?v=d4zLyf32e3I

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        final = []

        if (root is None):
            return []
        
        queue = deque()
        queue.append(root)

        while (len(queue) > 0):
            level = list(queue)
            innerList = []

            for nodeQ in level:
                nodeQ = queue.popleft()

                if (nodeQ):
                    if (nodeQ.left is not None):
                        queue.append(nodeQ.left)

                    if (nodeQ.right is not None):
                        queue.append(nodeQ.right)
  
                    innerList.append(nodeQ.val)

            final.append(innerList[-1])
        
        return final