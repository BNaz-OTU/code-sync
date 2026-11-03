# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: list[ListNode | None]) -> ListNode | None:
        heap = []

        for list1 in lists:
            while list1:
                val = list1.val
                heappush(heap, val)
                list1 = list1.next
        
        dummyNode = ListNode()
        head = dummyNode

        while heap:
            val = heappop(heap)
            node = ListNode(val)
            dummyNode.next = node
            dummyNode = dummyNode.next
        
        return head.next