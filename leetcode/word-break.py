class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        checker = [False] * (len(s) + 1)
        checker[-1] = True
        
        # print(checker)
        for idx in range(len(s) - 1, -1, -1):
            for word in wordDict:
                # print(f"Word: {word} | IDX: {idx} | nword: {s[idx : idx + len(word)]}")
                if (idx + len(word) <= len(s) and s[idx : idx + len(word)] == word and checker[idx + len(word)] == True):
                    # print("here")
                    checker[idx] = True
        
        # print(checker)
        return checker[0]