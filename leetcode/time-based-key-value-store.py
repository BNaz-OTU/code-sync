class TimeMap:

    def __init__(self):
        self.dictKeyToVal = {}
        self.dictKeyToTime = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if (key not in self.dictKeyToTime):
            self.dictKeyToTime[key] = [timestamp]
            self.dictKeyToVal[key] = [value]
        else:
            self.dictKeyToTime[key].append(timestamp)
            self.dictKeyToVal[key].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dictKeyToTime:
            return ""

        arr = self.dictKeyToTime[key]
        left = 0
        right = len(arr) - 1
        prev = None

        while (left <= right):
            middle = (left + right) // 2

            if (arr[middle] == timestamp):
                return self.dictKeyToVal[key][middle]
            
            elif (arr[middle] > timestamp):
                right = middle - 1
            
            else:
                prev = middle
                left = middle + 1
        
        if prev is  None:
            return ""
        
        return self.dictKeyToVal[key][prev]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)