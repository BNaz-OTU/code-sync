# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        targetFound = False
        currSum = 0

        def dfs(root, targetSum):
            if (root is None):
                print("Hi")
                return
            
            nonlocal currSum, targetFound
            currSum += root.val

            print(f"Root: {root} | Current Sum: {currSum}")

            if (currSum == targetSum and root.left is None and root.right is None):
                print("here 1")
                targetFound = True

            dfs(root.left, targetSum)
            dfs(root.right, targetSum)

            currSum -= root.val
                
        dfs(root, targetSum)
        return targetFound