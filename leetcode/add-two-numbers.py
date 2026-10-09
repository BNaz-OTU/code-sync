# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummy = ListNode()
        head = dummy
        carry = 0

        while l1 or l2 or carry:
            l1V, l2V = 0, 0

            if l1 is not None:
                l1V = l1.val
                l1 = l1.next
            
            if l2 is not None:
                l2V = l2.val
                l2 = l2.next
            
            total = l1V + l2V + carry

            num = total % 10
            dummy.next = ListNode(num)
            dummy = dummy.next
            carry = total // 10
        
        return head.next