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
        newHead = Node(0)
        final = newHead

        hashMap = {}

        while copy1:
            node = Node(copy1.val)
            hashMap[copy1] = node

            copy1 = copy1.next
        
        while copy2:
            # Grab the nodes
            currentNode = hashMap[copy2]
            nextNode = hashMap[copy2.next] if copy2.next else None
            randNode = hashMap[copy2.random] if copy2.random else None

            # Connect all components to the original node
            currentNode.next = nextNode
            currentNode.random = randNode

            # Move onto next Node in the list
            copy2 = copy2.next

            # Add new copy Node to final linked list
            newHead.next = currentNode
            newHead = newHead.next
        
        return final.next