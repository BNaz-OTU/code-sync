# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        heap = []
        
        def dfs(root):
            if root is None:
                return

            dfs(root.left)
            heap.append(root.val)
            dfs(root.right)
        
        dfs(root)
        heapify(heap)
        temp_k = k

        val = 0
        while temp_k > 0:
            temp_k -= 1
            val = heappop(heap)
        
        return val