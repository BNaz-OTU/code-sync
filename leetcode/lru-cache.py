class LinkList_DD:
    def __init__(self, key=None, val=None, prev=None, nxt=None):
        self.prev = prev
        self.nxt = nxt
        self.key = key
        self.val = val

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hashmap = {}

        self.left = LinkList_DD()
        self.right = LinkList_DD()

        self.left.nxt = self.right
        self.right.prev = self.left

    def remove(self, key):
        node = self.hashmap[key]

        # Grab next and prev nodes
        prev, nxt = node.prev, node.nxt

        # Disconnect from node
        prev.nxt = nxt
        nxt.prev = prev

        # Remove from the hashmap
        del self.hashmap[key]
    
    def insert(self, key, value):
        self.hashmap[key] = LinkList_DD(key, value)

        # Grab neighbor nodes
        nxt, prev = self.right, self.right.prev

        # Connect new node
        node = self.hashmap[key]
        node.nxt = nxt
        node.prev = prev

        # Connect to new node
        nxt.prev = node
        prev.nxt = node


    def get(self, key: int) -> int:
        if (key not in self.hashmap):
            return -1
        
        value = self.hashmap[key].val

        self.remove(key)
        self.insert(key, value)

        return value
        

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            self.remove(key)
        
        if (len(self.hashmap) >= self.capacity):
            lru = self.left.nxt
            self.remove(lru.key)

        self.insert(key, value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)