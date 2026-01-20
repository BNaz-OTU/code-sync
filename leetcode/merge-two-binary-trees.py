# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:           
        val = 0
        if (root1 is None and root2 is None):
            return

        elif (root1 is None and root2):
            val = root2.val
        
        elif (root2 is None and root1):
            val = root1.val
        
        else:
            val = root1.val + root2.val
        
        newTree = TreeNode(val)
        newTree.left = self.mergeTrees(root1.left if root1 else None, root2.left if root2 else None)
        newTree.right = self.mergeTrees(root1.right if root1 else None, root2.right if root2 else None)

        return newTree