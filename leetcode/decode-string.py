class Solution:
    def decodeString(self, s: str) -> str:
        # USED SOLN: https://www.youtube.com/watch?v=qB0zZpBJlh8
        stack = []

        for idx in range(len(s)):
            if (s[idx] != "]"):
                stack.append(s[idx])
            
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        
        return "".join(stack)