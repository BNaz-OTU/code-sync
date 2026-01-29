# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        hold_list = []

        def dfs(root):
            if (root is None):
                return 
            
            dfs(root.right)

            nonlocal hold_list
            hold_list.append(root.val)
            
            dfs(root.left)
        
        dfs(root)
        # print(hold_list)

        newRoot = TreeNode()
        head = newRoot
        while len(hold_list) > 0:
            newRoot.val = hold_list.pop()

            if (len(hold_list) == 0):
                break

            newRoot.right = TreeNode()
            newRoot = newRoot.right
        
        return head