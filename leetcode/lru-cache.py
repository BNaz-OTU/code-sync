class Node:

    def __init__(self, key=None, val=None, nxt=None, prev=None):
        self.key = key
        self.val = val
        self.nxt = nxt
        self.prev = prev

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashMap = {}
        self.left = Node()
        self.right = Node()

        self.left.nxt = self.right
        self.right.prev = self.left

    def _remove(self, node):
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev

    def _add(self, node):
        prev = self.right.prev
        prev.nxt = node
        node.prev = prev
        node.nxt = self.right
        self.right.prev = node

    def get(self, key: int) -> int:
        if (key in self.hashMap):
            node = self.hashMap[key]
            self._remove(node)
            self._add(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashMap:
            self._remove(self.hashMap[key])
        
        new_node = Node(key, value)
        self.hashMap[key] = new_node
        self._add(new_node)

        if len(self.hashMap) > self.capacity:
            lru = self.left.nxt
            self._remove(lru)
            del self.hashMap[lru.key]