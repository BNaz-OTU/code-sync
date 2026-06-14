# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummyNode = ListNode()
        head = dummyNode

        for miniList in lists:
            while miniList:
                val = miniList.val
                heappush(heap, val)
                miniList = miniList.next
        

        while heap:
            val = heappop(heap)
            node = ListNode(val)
            
            dummyNode.next = node
            dummyNode = dummyNode.next
        
        return head.next