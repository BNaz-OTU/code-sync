# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, node=0, left=None, right=None):
#         self.node = node
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        cur = root
        holder = deque()
        holder.append(cur)
        final = []

        while len(holder) > 0:
            temp = []
            for _ in range(len(holder)):
                node = holder.popleft()
                temp.append(node.val)

                if (node.left is not None):
                    holder.append(node.left)
                
                if (node.right is not None):
                    holder.append(node.right)
            
            final.append(temp)
        
        return final