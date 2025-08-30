class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for val in num:
            while (len(stack) > 0 and stack[-1] > val and k > 0):
                stack.pop()
                k -= 1
            
            stack.append(val)

        while (k > 0):
            k -= 1
            stack.pop()

        new_num = "".join(stack).lstrip('0')
        
        return str(new_num) if new_num != "" else '0'