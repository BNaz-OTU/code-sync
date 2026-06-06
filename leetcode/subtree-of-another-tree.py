# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def deeperdfs(root, subroot):
            if (root is None and subroot is None):
                return True
            
            if (root is None or subroot is None or root.val != subroot.val):
                return False
            
            return (deeperdfs(root.left, subroot.left) and deeperdfs(root.right, subroot.right))
            
        def dfs(root):
            if (root is None):
                return False
            
            if (root.val == subRoot.val):
                if (deeperdfs(root, subRoot)):
                    return True
            
            return (dfs(root.left) or dfs(root.right))
        
        return (dfs(root))