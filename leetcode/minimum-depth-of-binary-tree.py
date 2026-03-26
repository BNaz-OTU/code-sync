# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0

        min_depth = float('inf')
        
        def dfs(root, num):
            nonlocal min_depth
            
            if (root is None):
                return
            
            if (root.left is None and root.right is None):
                min_depth = min(min_depth, num + 1)
            
            dfs(root.left, num + 1)
            dfs(root.right, num + 1)
        
        dfs(root, 0)

        return min_depth