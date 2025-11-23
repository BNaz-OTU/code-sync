# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        # USED SOLN: https://www.youtube.com/watch?v=OnSn2XEQ4MY
        
        if not root:
            return None
        
        # Swap the children nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # Call for the next branches to be inverted
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root