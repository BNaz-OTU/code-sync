# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        final = []
        # found = []

        def inOrder(root):
            if (root is None):
                return
            
            inOrder(root.left)
            final.append(root.val)
            # print(f"Val: {root.val} | Length of List: {len(final)} | List: {final}")
            # if (len(final) == k):
            #     found.append(root.val)
            
            inOrder(root.right)
        
        inOrder(root)
        return final[k - 1]