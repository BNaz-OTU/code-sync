"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy1 = head
        copy2 = head
        dummyNode = ListNode(0)
        head2 = dummyNode
        hashmap = {}

        while copy1:
            hashmap[copy1] = ListNode(copy1.val)
            copy1 = copy1.next
        
        while copy2:
            node = hashmap[copy2]
            nextNode = hashmap[copy2.next] if copy2.next is not None else None
            randNode = hashmap[copy2.random] if copy2.random is not None else None

            node.next = nextNode
            node.random = randNode

            dummyNode.next = node
            dummyNode = dummyNode.next

            copy2 = copy2.next
        
        return head2.next