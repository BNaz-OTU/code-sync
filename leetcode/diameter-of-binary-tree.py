# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=K81C31ytOZE
        self.res = 0

        def dfs(root):
            if (root is None):
                return 0
            
            heightL = dfs(root.left)
            heightR = dfs(root.right)

            self.res = max(self.res, heightL + heightR)
            return max(heightL, heightR) + 1

        dfs(root)
        return self.res
        
    #     1
    #    /
    #   2