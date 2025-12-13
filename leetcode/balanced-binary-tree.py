# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if (root is None):
            return 0
        
        num1 = 1 + self.isBalanced(root.left)
        num2 = 1 + self.isBalanced(root.right)
        if (abs(num1 - num2) <= 1):
            return True
        else:
            return False