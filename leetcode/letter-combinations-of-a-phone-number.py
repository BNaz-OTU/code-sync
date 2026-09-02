class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        final = []

        def dfs(idx, text):
            if (len(text) == len(digits)):
                final.append(text)
                return
            
            for letter in letters[digits[idx]]:
                dfs(idx + 1, text + letter)
        
        dfs(0, "")
        return final