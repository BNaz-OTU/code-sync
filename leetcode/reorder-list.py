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
        head1 = head
        # 1. Get to the middle
        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        # 2. Reverse the Linked List from the middle
        prev = None
        second = slow.next
        # print(second)
        slow.next = None
        # print(second)
        # print(head)
        # print(slow)
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        # print(second)
        # print(slow)
        # print(prev)
        # print(head)
        r_list, f_list = prev, head
        while r_list:
            temp1 = f_list.next
            temp2 = r_list.next
            f_list.next = r_list
            r_list.next = temp1
            f_list = temp1
            r_list = temp2
        #     # 4, 3