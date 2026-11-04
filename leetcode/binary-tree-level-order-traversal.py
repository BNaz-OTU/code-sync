# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        if root is None:
            return []
            
        queue = deque()
        queue.append(root)
        final = []

        while queue:
            search = len(queue)
            temp = []

            for _ in range(search):
                node = queue.popleft()
                temp.append(node.val)

                if (node.left):
                    queue.append(node.left)
                
                if (node.right):
                    queue.append(node.right)
        
            final.append(temp)
        
        return final