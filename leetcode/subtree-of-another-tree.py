# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:
        def matchTree(root1, root2):
            if (root1 is None and root2 is None):
                return True
            
            if (root1 is None or root2 is None or root1.val != root2.val):
                return False
            
            return matchTree(root1.left, root2.left) and matchTree(root1.right, root2.right)
        
        def dfs(root):
            if (root is None):
                return False
            
            if (matchTree(root, subRoot)):
                return True
            
            return dfs(root.left) or dfs(root.right)
        
        return True if dfs(root) == True else False