class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        #  A - Z
        # 65 - 90

        # Flags:
        lower = False
        upper = False

        if (len(word) == 1):
            return True

        if (ord(word[0]) <= 90 and ord(word[1]) <= 90):
            # print('here')
            for idx in range(2, len(word)):
                if (ord(word[idx]) > 90):
                    return False

        elif (ord(word[0]) <= 90 and ord(word[1]) > 90):
            # print('here1')
            for idx in range(2, len(word)):
                if (ord(word[idx]) <= 90):
                    return False

        else:
            # print('here2')
            for idx in range(1, len(word)):
                if (ord(word[idx]) <= 90):
                    return False
        
        return True