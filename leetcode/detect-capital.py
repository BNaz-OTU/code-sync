class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitalCount = 0

        for idx in range(len(word)):
            if (ord(word[idx]) <= 90):
                capitalCount += 1

        if (capitalCount == len(word) or capitalCount == 0 or (capitalCount == 1 and ord(word[0]) <= 90)):
            return True
        
        return False