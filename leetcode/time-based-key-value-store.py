class TimeMap:

    def __init__(self):
        self.hashMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.hashMap):
            self.hashMap[key] = []
        
        self.hashMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        found = ""
        if key not in self.hashMap:
            return found
            
        left = 0
        right = len(self.hashMap[key]) - 1

        while left <= right:
            middle = (left + right) // 2

            if (self.hashMap[key][middle][0] <= timestamp):
                found = self.hashMap[key][middle][1]
                left = middle + 1
            
            else:
                right = middle - 1
        
        return found
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)