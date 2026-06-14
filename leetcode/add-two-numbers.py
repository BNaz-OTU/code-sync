# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        head = dummyNode
        carry = 0

        while l1 or l2 or carry:
            val1, val2, = 0, 0
            if (l1 is not None):
                val1 = l1.val
                l1 = l1.next
            
            if (l2 is not None):
                val2 = l2.val
                l2 = l2.next
            
            sumVal = val1 + val2 + carry
            finalVal = sumVal % 10
            carry = sumVal // 10

            node = ListNode(finalVal)
            dummyNode.next = node
            dummyNode = dummyNode.next
        
        return head.next