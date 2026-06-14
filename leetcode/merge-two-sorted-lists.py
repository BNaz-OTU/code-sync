# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = ListNode()
        head = dummyNode

        while list1 and list2:
            # print(list1)
            # print()
            # print(list2)
            # print("---------")
            if (list1.val <= list2.val):
                dummyNode.next = list1
                list1 = list1.next
            
            else:
                dummyNode.next = list2
                list2 = list2.next
            
            dummyNode = dummyNode.next
        
        if (list1 is not None):
            dummyNode.next = list1
        
        if (list2 is not None):
            dummyNode.next = list2
        
        return head.next