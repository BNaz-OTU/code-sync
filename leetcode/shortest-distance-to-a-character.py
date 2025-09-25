class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        final = []
        slow = 0 
        fast = 0
        let_found = None

        # Two Pointer Approach:
        # One pointer will go fast, while another pointer will go slow. The fast
        # pointer will be responsible for searching for the 'specific character'
        # while the slow character will keep track how far apart it is from the 'specific 
        # character' when it is found. When it locates the first instance of the 'specific 
        # character', it will mark its, location in 'let_found', for now the second loop
        # would only calculate the distance between, the first instance of the 'specific
        # character'. Once the 'fast pointer' locates another 'specific character', then
        # it will begin comparing the distance between the current 'specific character'
        # and the previous 'specific character' to determine which one is close given the current
        # position of the 'slow pointer/index'.

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

        # In the event that the 'specific character' doesn't show up at the end, the distance 
        # will be calculated/incremented by 1 each time it goes further away from 
        # the last seen 'specific character'
        if (len(final) != len(s)):
            count = 1
            while len(final) < len(s):
                final.append(count)
                count += 1
        
        return final