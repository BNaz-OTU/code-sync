class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        mono_stack = []

        for val in num:
            while (len(mono_stack) > 0 and mono_stack[-1] > val and k > 0):
                k -= 1
                mono_stack.pop()
            
            mono_stack.append(val)
        
        while (k > 0):
            mono_stack.pop()
            k -= 1
        
        final = "".join(mono_stack)
        final = final.lstrip('0')
        
        if (len(final) > 0):
            return final
        else:
            return '0'

        # return str(final)
        print(final)
        print(mono_stack)