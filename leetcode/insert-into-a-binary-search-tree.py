# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # Edge Case when the given tree is empty
        if root is None:
            return TreeNode(val)

        curr = root

        # Remembers the last connection
        prev = curr

        # Keep looping unitl we find the correct Node to do the insertion
        while (curr is not None):
            # Update the last connection
            prev = curr

            if (val < curr.val):
                # print(curr.val) # DEBUG
                curr = curr.left

            else:
                # print(curr.val) # DEBUG
                curr = curr.right
        
        # After leaving the loop use the last connection to determine where to place the new value
        if (val < prev.val):
            prev.left = TreeNode(val)
        else:
            prev.right = TreeNode(val)
        
        return root