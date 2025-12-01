# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if (not root):
            # print("Hello")
            return None
        
        if (root.val == val):
            # print(f"Found: {root.val}")
            return root

        elif (val < root.val):
            # print("Here 1")
            return self.searchBST(root.left, val)
        
        else:
            # print("Here 2")
            return self.searchBST(root.right, val)