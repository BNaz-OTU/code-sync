# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        dummyNode = ListNode()
        head2 = dummyNode

        while l1 or l2 or carry:
            op1, op2 = 0, 0

            if (l1 is not None):
                op1 = l1.val
                l1 = l1.next
            
            if (l2 is not None):
                op2 = l2.val
                l2 = l2.next
            
            total = op1 + op2 + carry
            carry = total // 10
            num = total % 10

            node = ListNode(num)
            dummyNode.next = node
            dummyNode = dummyNode.next
        
        return head2.next