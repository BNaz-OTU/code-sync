# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # ANOTHER SOLN: https://www.youtube.com/watch?v=uLVG45n4Sbg

        sumAll = 0

        def addNodes(root):
            if (root is None):
                return 
            
            nonlocal sumAll
            if (low <= root.val <= high):
                sumAll += root.val
            
            addNodes(root.left)
            addNodes(root.right)
            
            # if (root.val > low):
            #     return addNodes(root.left)
            
            # if (root.val < high):
            #     return addNodes(root.right)
            
            return sumAll
        
        return addNodes(root)