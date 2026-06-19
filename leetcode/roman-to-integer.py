class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I" : 1,
            "V" : 5, 
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        total = []
        for idx in range(len(s)):
            if (idx == 0):
                total.append(hashMap[s[idx]])
            
            elif (hashMap[s[idx - 1]] >= hashMap[s[idx]]):
                total.append(hashMap[s[idx]])
            
            else:
                cur = hashMap[s[idx]]
                prev = total[-1]
                total[-1] = cur - prev
        
        return sum(total)