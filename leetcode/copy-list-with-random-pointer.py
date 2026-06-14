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
        hashMap = {}

        while copy1:
            hashMap[copy1] = Node(copy1.val)
            copy1 = copy1.next
        
        dummyNode = Node(0)
        head2 = dummyNode
        while copy2:
            node = hashMap[copy2]
            nextNode = hashMap[copy2.next] if copy2.next is not None else None
            randNode = hashMap[copy2.random] if copy2.random is not None else None

            node.next = nextNode
            node.random = randNode

            dummyNode.next = node
            dummyNode = dummyNode.next

            copy2 = copy2.next
        
        return head2.next