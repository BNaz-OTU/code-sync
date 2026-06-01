# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def deepdfs(root, subRoot):
            if (root is None and subRoot is None):
                return True
            
            if (root is None or subRoot is None or root.val != subRoot.val):
                return False
            
            return deepdfs(root.left, subRoot.left) and deepdfs(root.right, subRoot.right)

        def dfs(root):
            if (root is None):
                return False
            
            if (root.val == subRoot.val and deepdfs(root, subRoot)):
                return True

            return dfs(root.left) or dfs(root.right)
        
        return dfs(root)