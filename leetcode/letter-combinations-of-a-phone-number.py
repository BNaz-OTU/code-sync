class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        final = []
        
        phone = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz"
        }

        def dfs(idx, string):
            if (idx == len(digits)):
                final.append(string)
                return

            currDigit = digits[idx]
            phoneVal = phone[currDigit]

            for char in phoneVal:
                dfs(idx + 1, string + char)
        
        dfs(0, "")
        return final