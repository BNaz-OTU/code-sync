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
        hashmap1 = {None : None}

        while copy1:
            hashmap1[copy1] = Node(copy1.val)
            copy1 = copy1.next
        
        dummyNode = Node(0)
        new_head = dummyNode
        copy2 = head
        while copy2:
            # Retrieve Nodes
            curr_node = hashmap1[copy2]
            next_node = hashmap1[copy2.next]
            rand_node = hashmap1[copy2.random]
            
            # Connect Nodes
            curr_node.next = next_node
            curr_node.random = rand_node

            dummyNode.next = curr_node
            dummyNode = dummyNode.next
            copy2 = copy2.next
        
        return new_head.next