# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        # USED SOLN: https://www.youtube.com/watch?v=JI71sxtHTng

        dummy = ListNode(-1, head)
        prev, curr = dummy, head

        while curr:
            n = curr.next

            if (curr.val == val):
                prev.next = n
            else:
                prev = curr
            
            curr = n
        
        return dummy.next