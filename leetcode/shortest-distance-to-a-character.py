class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        final = []

        slow = 0
        fast = 0
        found = None

        while fast < len(s):
            if (s[fast] == c):
                
                while slow < fast:
                    if (found is None):
                        final.append(fast - slow)

                    else:
                        minVal = min(abs(fast - slow), abs(found - slow))
                        final.append(minVal)
                    slow += 1
            
                found = fast
            
            fast += 1
        
        count = 0
        while (len(final) < len(s)):
            final.append(count)
            count += 1

        return final