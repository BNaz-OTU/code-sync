# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if (root is None):
            return []
            
        queue = deque()
        queue.append(root)
        final = []

        while len(queue) > 0:
            search = len(queue)
            temp = []
            for _ in range(search):
                node = queue.popleft()

                if (node.left is not None):
                    queue.append(node.left)
                
                if (node.right is not None):
                    queue.append(node.right)
                
                temp.append(node.val)
            
            final.append(temp)
        
        return final