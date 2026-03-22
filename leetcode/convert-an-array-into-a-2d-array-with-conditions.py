class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        hashMap = {}
        final = []

        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        print(hashMap)

        while len(hashMap) > 0:
            tempList = []
            list0 = []
            for key in hashMap:
                if (hashMap[key] != 0):
                    tempList.append(key)

                    hashMap[key] -= 1

                if (hashMap[key] == 0):
                    list0.append(key)

            
            while len(list0) > 0:
                hashMap.pop(list0[-1])
                list0.pop()            
            final.append(tempList)
        
        return final