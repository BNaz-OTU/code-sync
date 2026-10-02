# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        dummyNode = ListNode()
        head = dummyNode
        carry = 0

        while l1 or l2 or carry:
            l1Val, l2Val = 0, 0

            if (l1 is not None):
                l1Val = l1.val
                l1 = l1.next
            
            if (l2 is not None):
                l2Val = l2.val
                l2 = l2.next
            
            total = l1Val + l2Val + carry
            curr_num = total % 10
            carry = total // 10

            head.next = ListNode(curr_num)
            head = head.next
        
        return dummyNode.next