class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # USED SOLN: https://www.youtube.com/watch?v=0snEunUacZY
        final = []

        dictPhone = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"],
        }

        def backtrack(i, curStr):
            if (len(curStr) == len(digits)):
                final.append(curStr)
                return
            

            for char in dictPhone[digits[i]]:
                backtrack(i + 1, curStr + char)
        
        if (len(digits) > 0):
            backtrack(0, "")

        return final