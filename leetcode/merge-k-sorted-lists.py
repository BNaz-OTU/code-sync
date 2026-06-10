# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        newHead = ListNode()
        temp = newHead

        for listElement in lists:
            while listElement:
                heappush(heap, listElement.val)
                listElement = listElement.next
        
        while heap:
            val = heappop(heap)
            node = ListNode(val)
            temp.next = node
            temp = temp.next

        return newHead.next