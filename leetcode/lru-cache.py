class doubleLL:
    def __init__(self, key=0, val=0, nxt=None, prev=None):
        self.nxt = nxt
        self.prev = prev
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.left = doubleLL()
        self.right = doubleLL() 
        
        self.left.nxt = self.right
        self.right.prev = self.left
        
    def remove(self, node):
        prev, nxt = node.prev, node.nxt
        prev.nxt = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if (key not in self.cache):
            return -1
        
        node = self.cache[key]
        self.remove(node)
        
        prev = self.right.prev
        prev.nxt = node
        self.right.prev = node
        
        node.prev = prev
        node.nxt = self.right
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)

        elif (len(self.cache) == self.capacity):
            lru = self.left.nxt
            self.remove(lru)
            del self.cache[lru.key]

        node = doubleLL(key, value)
        self.cache[key] = node

        prev = self.right.prev

        prev.nxt, self.right.prev = node, node
        node.nxt, node.prev = self.right, prev
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)