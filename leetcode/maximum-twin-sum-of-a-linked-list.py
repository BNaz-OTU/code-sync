# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head
        prev = None
        maxVal = 0

        # while fast and fast.next:
        #     fast = fast.next.next
        #     slow = slow.next

        while fast and fast.next:
            fast = fast.next.next

            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        while slow:
            maxVal = max(maxVal, slow.val + prev.val)
            slow = slow.next
            prev = prev.next
        
        return maxVal

        print(slow)
        print(prev)
        # print(slow)