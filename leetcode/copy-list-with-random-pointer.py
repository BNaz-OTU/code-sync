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
        visit = {}
        newHead = Node(0)
        temp = newHead
        queue = deque()
        cur = head

        while cur:
            if cur in visit:
                continue
            else:
                queue.append(cur)
                visit[cur] = Node(cur.val)
            cur = cur.next
        
        while len(queue) > 0:
            old_node = queue.popleft()

            new_node = visit[old_node]
            new_rand_node = visit[old_node.random] if old_node.random is not None else None
            new_next_node = visit[old_node.next] if old_node.next is not None else None

            new_node.next = new_next_node
            new_node.random = new_rand_node

            temp.next = new_node
            temp = temp.next
        
        print(newHead)
        return newHead.next