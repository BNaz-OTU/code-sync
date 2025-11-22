# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        # USE FOR REFERENCE: https://www.youtube.com/watch?v=wgFPrzTjm7s

        list1 = ""
        list2 = ""

        # 1. Store each value in the nodes in a list
        while l1:
            list1 += str(l1.val)
            l1 = l1.next
        
        while l2:
            list2 += str(l2.val)
            l2 = l2.next
        
        # DEBUG
        print(f"List 1: {list1} | List 2: {list2}")

        # 2. Reverse the Lists and add them together
        r_list1 = list1[::-1]
        r_list2 = list2[::-1]

        total = int(r_list1) + int(r_list2)

        # DEBUG
        print(total)

        # 3. Convert to string, reverse the string and make a new linked list
        r_total = str(total)[::-1]

        # DEBUG
        print(r_total)
        temp = ListNode()
        head = temp

        print(temp.val, temp.next)

        for val in r_total:
            c = ListNode(val=int(val))
            temp.next = c
            temp = temp.next
        
        return head.next