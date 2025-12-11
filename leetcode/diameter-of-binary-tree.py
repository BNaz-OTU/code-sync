# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        # USED SOLN: https://www.youtube.com/watch?v=K81C31ytOZE
        
        if (root is None):
            return 0
        
        final = 0
        
        def dfs(root):
            if (root is None):
                return 0

            val_left = dfs(root.left)
            val_right = dfs(root.right)

            nonlocal final

            final = max(final, val_left + val_right)
            return 1 + max(val_left, val_right)
        
        dfs(root)
        return final