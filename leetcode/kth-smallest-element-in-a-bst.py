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
            if (root is None):
                return
            
            dfs(root.left)
            heap.append(root.val)
            dfs(root.right)
        
        dfs(root)
        print(heap)
        heapify(heap)
        temp_K = k

        while temp_K > 1:
            temp_K -= 1
            heappop(heap)
        
        return heap[0]