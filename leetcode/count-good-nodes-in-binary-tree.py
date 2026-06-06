# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(maxVal, root):
            nonlocal count
            if (root is None):
                return
            
            if (maxVal is None or root.val > maxVal):
                maxVal = root.val

            if (root.val >= maxVal):
                count += 1

            dfs(maxVal, root.left)
            dfs(maxVal, root.right)
        
        dfs(None, root)
        return count