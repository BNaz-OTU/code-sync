# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: TreeNode | None, subRoot: TreeNode | None) -> bool:

        def dfsComp(root1, root2):
            if (root1 is None and root2 is None):
                return True

            if ((root1 is  None) or (root2 is None) or (root1.val != root2.val)):
                return False
            
            return dfsComp(root1.left, root2.left) and dfsComp(root1.right, root2.right)
        
        def dfs(root, subRoot):
            if root is None:
                return 0

            if (root.val == subRoot.val and dfsComp(root, subRoot)):
                return 1
            
            return dfs(root.left, subRoot) or dfs(root.right, subRoot)
            
        
        return True if dfs(root, subRoot) == 1 else False