# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0

        def dfs(root, nodeList):
            nonlocal count

            if (root is None):
                return
            
            if (len(nodeList) == 0 or root.val >= max(nodeList)):
                count += 1
            
            nodeList.append(root.val)
            dfs(root.left, nodeList)
            dfs(root.right, nodeList)
            nodeList.pop()
        
        dfs(root, [])
        return count