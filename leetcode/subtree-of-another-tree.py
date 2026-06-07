# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def deeperdfs(root, subRoot):
            if (root is None and subRoot is None):
                return True
            
            if (root is None or subRoot is None or root.val != subRoot.val):
                return False
            
            return (deeperdfs(root.left, subRoot.left) and deeperdfs(root.right, subRoot.right))

        def dfs(root, subRoot):
            if (root is None):
                return False
            
            if (root.val == subRoot.val and deeperdfs(root, subRoot)):
                return True
            
            return (dfs(root.left, subRoot) or dfs(root.right, subRoot))
        
        return dfs(root, subRoot)