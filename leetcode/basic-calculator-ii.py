class Solution:
    def calculate(self, s: str) -> int:
        # USED SOLN: https://www.youtube.com/watch?v=W3Rg4HVSZ9k
        idx = 0

        cur = prev = res = 0
        cur_oper = "+"

        while idx < len(s):
            cur_char = s[idx]

            if (cur_char.isdigit()):
                while (idx < len(s) and s[idx].isdigit()):
                    cur = cur * 10 + int(s[idx])

                    idx += 1
                
                idx -= 1

                if cur_oper == "+":
                    res += cur
                    prev = cur
                
                elif cur_oper == "-":
                    res -= cur
                    prev = -cur
                
                elif cur_oper == "*":
                    res -= prev
                    res += prev * cur

                    prev = cur * prev
                
                else:
                    res -= prev
                    res += int(prev / cur)

                    prev = int(prev / cur)
                
                cur = 0
            
            elif cur_char != " ":
                cur_oper = cur_char

            idx += 1
        
        return res