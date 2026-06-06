# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        final = []

        def dfs(root):
            if (root is None):
                return 
            
            dfs(root.left)
            final.append(root.val)
            dfs(root.right)
        
        dfs(root)
        
        for idx in range(len(final)):
            if (idx == k - 1):
                return final[idx]