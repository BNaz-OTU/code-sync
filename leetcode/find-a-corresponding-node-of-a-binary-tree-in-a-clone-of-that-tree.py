# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # USED SOLN: https://www.youtube.com/watch?v=ejXTsnWeoyU

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def dfs(og_node, c_node):
            if (og_node is None):
                return 

            # print(id(og_node), id(target))
            # print(og_node)
            if (og_node == target):
                return c_node
            
            return dfs(og_node.left, c_node.left) or dfs(og_node.right, c_node.right)
        
        # print(target)
        return dfs(original, cloned)