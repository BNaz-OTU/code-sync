# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for miniList in lists:
            while miniList:
                heappush(heap, miniList.val)
                miniList = miniList.next
        
        dummyNode = ListNode()
        head = dummyNode

        while heap:
            val = heappop(heap)

            node = ListNode(val)
            dummyNode.next = node
            dummyNode = dummyNode.next

        return head.next