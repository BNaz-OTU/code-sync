# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, path):
            nonlocal count
            # print (root, path)
            # print()
            if (root is None):
                return 
            
            # if (len(path) == 0):
            path.append(root.val)
            
            if (root.val >= max(path)):
                count += 1
            
            dfs(root.left, path.copy())
            dfs(root.right, path.copy())
        
        dfs(root, [])
        return count