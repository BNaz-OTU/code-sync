# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        dummyNode = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None 
        slow2 = slow.next
        slow.next = None

        while slow2:
            temp = slow2.next
            slow2.next = prev
            prev = slow2
            slow2 = temp
        
        while prev:
            temp1 = dummyNode.next
            temp2 = prev.next
            dummyNode.next = prev
            dummyNode = dummyNode.next
            dummyNode.next = temp1
            dummyNode = dummyNode.next
            prev = temp2