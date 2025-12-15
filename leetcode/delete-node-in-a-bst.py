# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return root

        # print(root.val, key)
        if (key < root.val):
            root.left = self.deleteNode(root.left, key)
        
        elif (key > root.val):
            root.right = self.deleteNode(root.right, key)
        
        else:
            if (root.right is None):
                return root.left

            elif (root.left is None):
                return root.right

            else:
                minimumNode = self.minimum(root.right)
                root.val = minimumNode.val
                # print(root)
                # print(root.right)
                # print("Second Loop")
                root.right = self.deleteNode(root.right, minimumNode.val)
                return root
        
        return root
        
    def minimum(self, root):
        root = root
        while root and root.left:
            root = root.left
        return root
    
    # self.minimum(root)