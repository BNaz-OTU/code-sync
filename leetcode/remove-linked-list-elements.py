# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # curr = head
        dummyNode = ListNode()
        dummyNode.next = head

        curr = dummyNode
        print(curr)
        while curr:
            # print
            while (curr.next and curr.next.val == val):
                curr.next = curr.next.next
        
            curr = curr.next

        return dummyNode.next