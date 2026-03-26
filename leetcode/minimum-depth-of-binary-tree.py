# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# USED SOLN: https://www.youtube.com/watch?v=My9ZyeCh_wE
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if (root is None):
            return 0
        
        self.min_depth = float('inf')

        self.dfs(root, 0)

        return self.min_depth

    def dfs(self, node, cur_depth):
        if (node is None):
            return
        
        if (node.left is None and node.right is None):
            self.min_depth = min(self.min_depth, cur_depth + 1)
        
        self.dfs(node.left, cur_depth + 1)
        self.dfs(node.right, cur_depth + 1)