class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        final = []
        slow = 0 
        fast = 0
        let_found = None

        while fast < len(s):
            if (s[fast] == c):
                # print(f"FOUND {c}")
                while slow <= fast:
                    if (let_found is None):
                        final.append(fast - slow)
                
                    else:
                        small = min(abs(fast - slow), abs(let_found - slow))
                        final.append(small)

                    slow += 1

                let_found = fast
                fast += 1

            else:
                fast += 1

        if (len(final) != len(s)):
            count = 1
            while len(final) < len(s):
                final.append(count)
                count += 1
        
        return final