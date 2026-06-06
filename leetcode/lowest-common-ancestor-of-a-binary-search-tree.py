# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        def dfs(root):
            if (root is None):
                return
            
            if ((root.val >= p.val and root.val <= q.val) or (root.val <= p.val and root.val >= q.val)):
                return root
            
            if (p.val > root.val and q.val > root.val):
                return dfs(root.right)
            
            if (p.val < root.val and q.val < root.val):
                return dfs(root.left)
        
        return dfs(root)