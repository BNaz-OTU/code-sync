class Node:

    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.right = Node() # Most Used
        self.left = Node() # Least Used

        self.left.nxt = self.right
        self.right.prev = self.left

        self.hashMap = {}
    
    def _remove(self, node):
        # # Get the node
        # node = self.hashMap[key]

        # Get previous node and next node
        prev = node.prev
        nxtv = node.nxt
        
        # Disconnecting from current node: Set the previous node to point to next and vice-versa
        prev.nxt = nxtv
        nxtv.prev = prev
        pass
    
    def _add(self, node):
        # Get the old recently added node
        prev = self.right.prev

        # Connecting the newly added node the second node
        prev.nxt = node
        node.prev = prev

        # Connecting the newly added node to the right node
        node.nxt = self.right
        self.right.prev = node


    def get(self, key: int) -> int:
        if key in self.hashMap:
            value = self.hashMap[key].val
            self._remove(self.hashMap[key])
            self._add(self.hashMap[key])
            return value
        
        return -1

    def put(self, key: int, value: int) -> None:
        if (key in self.hashMap):
            self._remove(self.hashMap[key])

        self.hashMap[key] = Node(key, value)
        self._add(self.hashMap[key])
        
        if (len(self.hashMap) > self.capacity):
            lru = self.left.nxt
            self._remove(lru)
            del self.hashMap[lru.key]
        
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)