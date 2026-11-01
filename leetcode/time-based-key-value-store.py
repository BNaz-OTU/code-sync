class TimeMap:

    def __init__(self):
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.hashmap):
            self.hashmap[key] = []

        self.hashmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.hashmap):
            return ""
        
        KeyList = self.hashmap[key]

        left, right = 0, len(KeyList) - 1
        found = ""
        while left <= right:
            middle = (left + right) // 2

            if (KeyList[middle][0] == timestamp):
                return KeyList[middle][1]
            
            elif (KeyList[middle][0] > timestamp):
                right = middle - 1
            
            else:
                found = KeyList[middle][1]
                left = middle + 1
        
        return found
        
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)