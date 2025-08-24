class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        fast = 0 
        slow = None
        new_list = []
        stack = []

        while fast < len(s):
            if (s[fast] == c):
                stack.append(fast)
                temp = stack[::-1]

                while len(temp) > 0:
                    if (slow is None):
                        new_list.append(fast - temp.pop())
                    else:
                        curr_idx = temp.pop()
                        dist = min(abs(curr_idx - slow), abs(fast - curr_idx))
                        new_list.append(dist)

                stack = [] 
                slow = fast

            else:
                stack.append(fast)
            
            fast += 1
        
        if (len(stack) > 0):
            for val in stack:
                new_list.append(val - slow)
        
        return new_list