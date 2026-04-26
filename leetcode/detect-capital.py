class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitalNum = 0
        
        for let in word:
            if (ord(let) <= 90):
                capitalNum += 1
        
        if (capitalNum == 0 or capitalNum == len(word) or (capitalNum == 1 and ord(word[0]) <= 90)):
            return True
        return False

        # print("A", ord("A"))
        # print("Z", ord("Z"))
        # print("a", ord("a"))
        # print("z", ord("z"))