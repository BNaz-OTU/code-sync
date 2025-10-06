class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = "qwertyuiop"
        row2 = "asdfghjkl"
        row3 = "zxcvbnm"
        final = []

        for word in words:
            flag = False
            for idx in range(len(word)):
                if (word[0].lower() in row1 and word[idx].lower() not in row2 and word[idx].lower() not in row3):
                    continue
                elif (word[0].lower() in row2 and word[idx].lower() not in row1 and word[idx].lower() not in row3):
                    continue
                elif (word[0].lower() in row3 and word[idx].lower() not in row1 and word[idx].lower() not in row2):
                    continue
                else:
                    flag = True
            
            if (flag == False):
                final.append(word)
        
        return final