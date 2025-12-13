# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if (root is None):
            return []

        queue = deque()
        final = []

        queue.append(root)

        while (len(queue) > 0):
            len_q = len(queue)
            levels = []

            for _ in range(len_q):
                node = queue.popleft()

                levels.append(node.val)

                if (node.left is not None):
                    queue.append(node.left)

                if (node.right is not None):
                    queue.append(node.right)
            
            final.append(levels[-1])
                
        return final