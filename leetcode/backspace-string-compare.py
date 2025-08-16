class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        # Space of O(1) solution: https://www.youtube.com/watch?v=k2qrymM_DOo
        
        stack_s = []
        stack_t = []

        for val in s:
            if (val == '#' and len(stack_s) != 0):
                stack_s.pop()
            elif (val == '#' and len(stack_s) == 0):
                continue
            else:
                stack_s.append(val)
        
        for val in t:
            if (val == '#' and len(stack_t) != 0):
                stack_t.pop()
            elif (val == '#' and len(stack_t) == 0):
                continue
            else:
                stack_t.append(val)
        
        print(f's : {stack_s} | t : {stack_t}')

        return stack_s == stack_t