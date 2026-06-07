# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        final = None

        def dfs(root):
            nonlocal count, final
            if (root is None):
                return
            
            dfs(root.left)
            
            count += 1
            if (count == k):
                final = root.val
                return

            dfs(root.right)
        
        dfs(root)
        return final