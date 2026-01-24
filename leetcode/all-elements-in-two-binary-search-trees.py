# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ANOTHER METHOD: https://www.youtube.com/watch?v=3nn6DJIZXfs
    def getAllElements(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> List[int]:
        list1 = []
        list2 = []
        final = []
        
        def dfs(root, someList):
            if (root is None):
                return
            
            dfs(root.right, someList)
            someList.append(root.val)
            dfs(root.left, someList)

        dfs(root1, list1)
        dfs(root2, list2)

        print(list1)
        print(list2)

        while len(list1) > 0 and len(list2) > 0:
            if (list1[-1] < list2[-1]):
                final.append(list1.pop())
            else:
                final.append(list2.pop())
        
        while len(list1) > 0:
            final.append(list1.pop())
        
        while len(list2) > 0:
            final.append(list2.pop())
        
        return final

        # r_list1 = list1[::-1]
        # r_list2 = list2[::-1]
        # list1Idx = 0
        # list2Idx = 0

        # while list1Idx < len(list1) or list2Idx < len(list2):
        #     if list1[list1Idx] < list2[list2Idx]:
        #         final.append(list1[list1Idx])
        #         list1Idx += 1
        #     else:
        #         final.append(list2[list2Idx])
        #         list2Idx += 1
        
        # return final