class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        temp = ""
        num = ""

        for val in s:
            if (val == ']'):
                while stack[-1] != '[':
                    char = stack.pop()[::-1]
                    temp += char
                
                stack.pop()

                while (len(stack) > 0 and stack[-1].isdigit()):
                    num += stack.pop()
                
                new_val = int(num[::-1]) * temp
                stack.append(new_val[::-1])
                num = ""
                temp = ""
            else:
                stack.append(val)

        return "".join(stack)