# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        valList = []

        def dfs(root):
            if (root is None):
                return 
            
            dfs(root.left)
            valList.append(root.val)
            dfs(root.right)

        dfs(root)

        for idx in range(0, len(valList) - 1):
            low = valList[idx]
            high = valList[idx + 1]

            print(f"Low: {low} | High: {high}")

            if (low > high or low == high):
                return False 
        
        return True