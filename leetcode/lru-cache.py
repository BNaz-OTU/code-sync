class Node: 
    def __init__(self, key=0, val=0, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt


class LRUCache:

    def __init__(self, capacity: int):
        self.hashMap = {}
        self.cap = capacity

        # Least used
        self.left = Node()

        # Most used
        self.right = Node()

        # Make the connection
        self.left.nxt = self.right
        self.right.prev = self.left
    
    def remove(self, key):
        node = self.hashMap[key]

        prev = node.prev 
        nxt = node.nxt

        prev.nxt, nxt.prev = nxt, prev
    
    def insert(self, key, value):
        node = Node(key, value)

        prev = self.right.prev

        # Connect the new node
        node.prev = prev
        node.nxt = self.right

        # Connect the other nodes to new node
        self.right.prev = node
        prev.nxt = node
        
        self.hashMap[key] = node

    def get(self, key: int) -> int:
        if (key in self.hashMap):
            value = self.hashMap[key].val
            self.remove(key)
            self.insert(key, value)
            return self.hashMap[key].val
        
        return -1
        

    def put(self, key: int, value: int) -> None:
        if (key in self.hashMap):
            self.remove(key)
        
        self.insert(key, value)

        if (len(self.hashMap) > self.cap):
            least = self.left.nxt
            self.remove(least.key)

            del self.hashMap[least.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)