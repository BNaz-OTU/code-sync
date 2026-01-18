# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(root, target):
            if (root is None):
                return 

            if (root.val == target.val):
                return root
            
            return dfs(root.left, target) or dfs(root.right, target)
        
        return dfs(cloned, target)