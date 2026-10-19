class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        checker = [False] * (len(s) + 1)
        checker[-1] = True
        
        for idx in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # print(f"IDX: {idx} | Word: {word} | Char slice: {s[idx : idx + len(word)]} | Prev Idx: {idx + len(word)}")
                if (idx + len(word) <= len(s) and s[idx : idx + len(word)] == word and checker[idx + len(word)] == True):
                    checker[idx] = True
            
        
        return checker[0]