# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        # USED SOLN: https://www.youtube.com/watch?v=3TXclW6KTKA
        final = []
        path = []


        def dfs(root, path):
            if (root is None):
                return

            if (root.left is None and root.right is None):
                path.append(root.val)
                final.append("->".join(str(p) for p in path))
                path.pop()
                return

            path.append(root.val)
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, path)
        return final