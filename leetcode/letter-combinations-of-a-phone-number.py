class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # USED SOLN: https://www.youtube.com/watch?v=0snEunUacZY

        letToNum = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }

        final = []

        def backtrack(idx, curStr):
            if (len(curStr) == len(digits)):
                final.append(curStr)
                return
            
            for char in letToNum[digits[idx]]:
                backtrack(idx + 1, curStr + char)
        
        if (len(digits) > 0):
            backtrack(0, "")

        return final