# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        carry = 0
        dummyNode = ListNode()
        head = dummyNode

        while l1 or l2 or carry:
            l1Val, l2Val = 0, 0

            if (l1 is not None):
                l1Val = l1.val
                l1 = l1.next
            
            if (l2 is not None):
                l2Val = l2.val
                l2 = l2.next
            
            n_val = l1Val + l2Val + carry
            carry = n_val // 10
            num = n_val % 10

            node = ListNode(num)
            dummyNode.next = node
            dummyNode = dummyNode.next
        
        return head.next