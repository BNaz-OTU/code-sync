# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            if (root is None):
                return [True, 0]

            left, right = dfs(root.left), dfs(root.right)
            # In "(left[0] and right[0])" it determines whether the previous trees/branches were already balanced
            # In "(abs(left[1] - right[1]) <= 1)" it checks whether the height of the balanced tree isn't more 
            #    than 1, otherwise its unbalanced
            # Combining those 2 statements together, it will determine if the tree was balanced
            
            balanced = ((left[0] and right[0]) and (abs(left[1] - right[1]) <= 1))
            
            return [balanced, max(left[1], right[1]) + 1]
        
        return dfs(root)[0]