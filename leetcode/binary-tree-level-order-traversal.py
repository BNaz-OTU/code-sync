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

        queue = deque()
        queue.append(root)
        final = []

        while len(queue) > 0:
            # print(queue)
            # print()
            temp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if (node is None):
                    continue
                
                temp.append(node.val)
                queue.append(node.left)
                queue.append(node.right)

            final.append(temp)
        
        return final[:-1]