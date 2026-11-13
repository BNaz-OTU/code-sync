# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []
            
        final = []
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            tmp = None
            search = len(queue)

            for _ in range(search):
                node = queue.popleft()

                if (node.left is not None):
                    queue.append(node.left)
                
                if (node.right is not None):
                    queue.append(node.right)
                
                tmp = node.val
            
            final.append(tmp)

        return final