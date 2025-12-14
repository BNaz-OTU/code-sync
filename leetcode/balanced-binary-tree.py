# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if (root is None):
                return 0
        
            heightL = dfs(root.left)
            if (heightL == -1):
                return -1
            
            heightR = dfs(root.right)
            if (heightR == -1):
                return -1
            
            if (abs(heightL - heightR) <= 1):
                return max(heightL, heightR) + 1
            else:
                return -1
        
        print(dfs(root))
        return dfs(root) != -1