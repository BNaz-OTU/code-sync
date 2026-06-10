# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if (list1 is None and list2 is None):
            return None
        
        dummyNode = ListNode()
        head = dummyNode

        while list1 and list2:
            if (list1.val <= list2.val):
                temp = list1.next
                dummyNode.next = list1
                list1.next = list2
                list1 = temp
                dummyNode = dummyNode.next
            else:
                temp = list2.next
                dummyNode.next = list2
                list2.next = list1
                list2 = temp
                dummyNode = dummyNode.next
        
        if list1 is None and list2 is None:        
            return head.next
        
        if list1 is None and list2 is not None:
            dummyNode.next = list2
            return head.next
        
        if list2 is None and list1 is not None:
            dummyNode.next = list1
            return head.next