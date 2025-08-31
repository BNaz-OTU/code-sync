# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            # Copy the nodes ahead
            nxt = curr.next

            # Update the current node to the previous node
            curr.next = prev

            # Move the prev node to the current node, so the chaining can continue
            prev = curr

            # Continue moving through the linked list
            curr = nxt
        
        return prev