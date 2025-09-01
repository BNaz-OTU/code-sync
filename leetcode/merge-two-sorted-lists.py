# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        dummyNode = ListNode()
        head = dummyNode

        while curr1 or curr2:

            if (curr2 is None):
                dummyNode.next = curr1
                dummyNode = dummyNode.next
                curr1 = curr1.next
                print('Here 1')
            
            elif (curr1 is None):
                dummyNode.next = curr2
                dummyNode = dummyNode.next
                curr2 = curr2.next
                print('Here 2')

            elif (curr1.val < curr2.val):
                dummyNode.next = curr1
                dummyNode = dummyNode.next
                curr1 = curr1.next

                print("#1 --------")
                print(dummyNode)
                print(curr1)

            elif (curr1.val > curr2.val):
                dummyNode.next = curr2
                dummyNode = dummyNode.next
                curr2 = curr2.next

                print("#2 --------")
                print(dummyNode)
                print(curr2)
            
            elif (curr1.val == curr2.val):
                dummyNode.next = curr1
                dummyNode = dummyNode.next
                curr1 = curr1.next

                print("#EQUAL --------")
                print(dummyNode)
                print(curr1)
            

            print("------------")
            print(f"HEAD:{head}")
            
        return head.next