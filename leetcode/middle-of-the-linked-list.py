# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr1 = head
        curr2 = head
        counter = 0
        count2 = 0

        while curr1:
            print(curr1.val)
            counter += 1
            curr1 = curr1.next
        
        ranger = counter // 2
        
        while count2 < ranger:
            count2 +=1
            curr2 = curr2.next
        
        return curr2