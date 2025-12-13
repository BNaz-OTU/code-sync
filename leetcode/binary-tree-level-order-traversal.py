# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        final = []
        queue = deque()
        queue.append(root)

        while (len(queue) > 0):
            levels = []
            curr_q = queue
            for _ in range(len(curr_q)):
                node = queue.popleft()
                levels.append(node.val)

                if (node.left):
                    queue.append(node.left)
                if (node.right):
                    queue.append(node.right)
            
            final.append(levels)
        
        return final