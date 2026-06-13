class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (len(t) > len(s)):
            return ""
        
        countT = {}
        countS = {}
        minLen = len(s) + 1
        word = [-1, -1]

        for char in t:
            if (char not in countT):
                countT[char] = 0
            
            countT[char] += 1
                
        left, right = 0, 0

        matches = 0
        for right in range(len(s)):
            val = s[right]
            countS[val] = 1 + countS.get(val, 0)

            if (val in countT and countS[val] == countT[val]):
                matches += 1

            # print(countT, countS)
            # print(matches)
            while matches == len(countT):
                end_val = s[left]

                if (minLen > (right - left + 1)):
                    minLen = right - left + 1
                    word = [left, right]
                
                countS[end_val] -= 1
                if (end_val in countT and countS[end_val] < countT[end_val]):
                    matches -= 1
                
                left += 1
            
            
        return s[word[0]:word[1] + 1]