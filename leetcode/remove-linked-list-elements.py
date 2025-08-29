# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # Setup dummynode so its connected to the head
        dummyNode = ListNode(next=head)

        # Readjust the position/index of head so its at the beginning since dummynode was added
        head = dummyNode

        # Create a temp copy to iterate through the linked list
        curr = head

        while (curr):
            while (curr.next and curr.next.val == val):
                curr.next = curr.next.next
            
            curr = curr.next
        
        return head.next