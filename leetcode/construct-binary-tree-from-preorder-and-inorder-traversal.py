# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        set_check_pre = set()
        set_check_ord = set()

        # Start with checking the preorder, since that always shows the root

        root = TreeNode(preorder[0])
        curr = root
        final = root

        # After creating the root node, add the node to a set so that I know when
        # to stop iterating through the inorder
        set_check_pre.add(preorder[0])

        idx = 0
        for idx in range(len(inorder)):
            set_check_ord.add(inorder[idx])
            if (inorder[idx] in set_check_pre):
                break
        
        new_list = inorder[:idx]
        new_list = new_list[::-1]
        updated_inorder = inorder[idx + 1:]
        print(updated_inorder)

        return
        print(new_list)
        # Create left branch of the tree
        for val in newlist:
            curr.left = TreeNode(val)
            curr = curr.left
        
        # Iterate through the preorder list to find the right tree ignore values found in left 
        # using a set of already found values from inorder list
        root = root.right
        curr = root

        # for val in