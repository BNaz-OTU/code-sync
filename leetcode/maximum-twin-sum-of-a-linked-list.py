# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # t: 0, 0, 0, 0, 0, 0
        # n: 1, 2, 3, 4, 5, 6
        # i: 0, 1, 2, 3, 4, 5
        list_nums = []

        while head:
            list_nums.append(head.val)
            head = head.next
        
        maxNum = 0
        left, right = 0, len(list_nums) - 1

        while left < right:
            maxNum = max(maxNum, list_nums[left] + list_nums[right])
            left += 1
            right -= 1
        
        return maxNum