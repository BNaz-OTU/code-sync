class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        substring = []
        set_str = set()
        final = 0

        for idx in range(len(s)):
            while s[idx] in set_str:
                let = substring.pop(0)
                set_str.remove(let)
            
            set_str.add(s[idx])
            substring.append(s[idx])

            if (len(set_str) == 3):
                final += 1

            elif (len(set_str) == 4):
                final += 1
                let = substring.pop(0)
                set_str.remove(let)

        return final