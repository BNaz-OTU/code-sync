class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        final = []

        for idx, val in enumerate(words):
            if (x in val):
                final.append(idx)
            # print(idx, val)
        
        return final