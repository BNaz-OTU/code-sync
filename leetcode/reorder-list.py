# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # print(f'Fast: {fast}')
        # print(f"Slow: {slow}")
        # print(f"Head: {head}")

        last_half = slow.next
        slow.next = None
        prev = None

        # print(slow)
        # print(head)
        # print(last_half)

        while last_half:
            temp_next = last_half.next
            last_half.next = prev
            prev = last_half
            last_half = temp_next
        
        # print(prev)
        # print(slow)
        # print(head)

        # print

        first, second = head, prev

        while second:
            temp_1, temp_2 = first.next, second.next
            first.next = second
            second.next = temp_1
            first, second = temp_1, temp_2

        # [1, 2,` 3]
        #  | /
        # [4, 3]`
        
        # ---------------------------------------------------------------------------------------------------
        """
        # Find the middle
        slow = head
        fast = head.next

        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next
        
        print(fast)
        print(slow)

        # Reverse second half
        second = slow.next
        slow.next = None
        prev = None

        print("--------------")
        print(f"Second: {second}")
        print(f"Slow: {slow} | Slow.next: {slow.next}")
        print(f"Prev: {prev}")

        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp
        
        # Merge two halfs
        first = head
        second = prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
        """