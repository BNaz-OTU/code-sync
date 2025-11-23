# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        set_link = set()

        while headA:
            if (headA not in set_link):
                set_link.add(headA)
            
            headA = headA.next
        
        while headB:
            if (headB in set_link):
                return headB

            headB = headB.next

        return None