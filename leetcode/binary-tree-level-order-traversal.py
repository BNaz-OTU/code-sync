# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if (root is None):
            return []

        final = []
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            temp = []
            
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if (node.left is not None):
                    queue.append(node.left)
                
                if (node.right is not None):
                    queue.append(node.right)

                temp.append(node.val)
            
            final.append(temp)
        
        return final