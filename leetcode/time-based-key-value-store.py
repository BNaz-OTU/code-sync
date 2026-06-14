class TimeMap:

    def __init__(self):
        self.hashMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.hashMap):
            self.hashMap[key] = []
        
        self.hashMap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        if (key not in self.hashMap):
            return ""
            
        arr = self.hashMap[key]

        left = 0
        right = len(arr) - 1
        word = ""

        while left <= right:
            middle = (left + right) // 2

            if (arr[middle][0] == timestamp):
                return arr[middle][1]
            
            elif (arr[middle][0] > timestamp):
                right = middle - 1
            
            else:
                left = middle + 1
                word = arr[middle][1]
        
        return word



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)