class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_let = {
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

        def dfs_let(idx, comb):
            if (len(comb) == len(digits)):
                final.append(comb)
                return 
            for cur in num_to_let[digits[idx]]:
                dfs_let(idx + 1, comb + cur)
        
        if digits:
            dfs_let(0, "")
            
        return final