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
        final = []
        queue = deque()
        queue.append(root)

        while (len(queue) > 0):
            levels = []
            len_q = len(queue)

            for _ in range(len_q):
                node = queue.popleft()

                if (node.left):
                    queue.append(node.left)
                
                if (node.right):
                    queue.append(node.right)
                
                levels.append(node.val)
            
            final.append(levels[-1])
        
        return final