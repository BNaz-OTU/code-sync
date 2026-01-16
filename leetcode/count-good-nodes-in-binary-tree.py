# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # Another method: https://www.youtube.com/watch?v=7cp5imvDzl4 

    def goodNodes(self, root: TreeNode) -> int:
        countGoodNodes = 0
        arr = []

        def dfs(root):
            if (root is None):
                return
            
            nonlocal arr, countGoodNodes

            arr.append(root.val)
            # print(arr, max(arr))

            if (max(arr) <= root.val):
                countGoodNodes += 1

            dfs(root.left)
            dfs(root.right)
            arr.pop()
        
        dfs(root)
        return countGoodNodes