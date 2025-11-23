# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        # USED REFERENCE: https://www.youtube.com/watch?v=D0X0BONOQhI

        # Declare Variables
        tempA = headA
        tempB = headB
        lengthA = 0
        lengthB = 0

        # 1. Determine the Length of each Linked List
        while headA:
            lengthA += 1
            headA = headA.next
        
        while headB:
            lengthB += 1
            headB = headB.next

        # 2. If they have different lengths update the linked list, so that they 
        # both have the same starting point
        while (lengthA > lengthB):
            tempA = tempA.next
            lengthA -= 1
        
        while (lengthB > lengthA):
            tempB = tempB.next
            lengthB -= 1
        
        # 3. Find the Intersecting Node
        while tempA:
            if (tempA == tempB):
                return tempA
            
            tempA = tempA.next
            tempB = tempB.next

        return None