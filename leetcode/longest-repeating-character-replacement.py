class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 0
        hashChar = {}
        maxLen = 0

        while right < len(s):
            if (s[right] in hashChar):
                hashChar[s[right]] += 1
            
            else:
                hashChar[s[right]] = 1
            
            largestChar = max(hashChar.values())
            # print(hashChar, s[right], largestChar)
            while (right - left + 1) - largestChar > k:
                hashChar[s[left]] -= 1

                if (hashChar[s[left]] == 0):
                    del hashChar[s[left]]
                
                largestChar = max(hashChar.values())
                left += 1

            maxLen = max(maxLen, right - left + 1)
            right += 1

        return maxLen