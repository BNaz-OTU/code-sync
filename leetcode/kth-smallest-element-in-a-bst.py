# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        tempList = []

        def dfs(root):
            if (root is None):
                return
            
            dfs(root.left)
            tempList.append(root.val)
            dfs(root.right)
        
        dfs(root)
        return tempList[k - 1]