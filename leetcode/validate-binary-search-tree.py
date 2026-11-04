# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        
        def dfs(root, left, right):
            if (root is None):
                return True
            
            if not (root.val < right and root.val > left):
                return False
            
            return (dfs(root.left, left, root.val) and dfs(root.right, root.val, right))
        
        return dfs(root, float("-inf"), float("inf"))