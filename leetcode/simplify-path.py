class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        final = ''

        new_path = path.split('/')
        # print(new_path)

        for val in new_path:
            if (val == '..' and len(stack) > 0):
                stack.pop()
            elif (val == '.' or val == '' or val == '..'):
                continue
            else:
                stack.append(val)
        
        for val in stack:
            final += '/' + val

        return final if len(final) != 0 else '/'