class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # DIDNT USE SOLN, ONLY CHECKED FOR REFERENCE: https://www.youtube.com/watch?v=lfqaq3nfGZQ
        count = 0
        s_list = list(s)

        if (len(s) < k):
            return s[::-1]

        while count < len(s):
            left = count
            right = count + k - 1

            if (right > len(s)):
                right = len(s) - 1

            while(left < right):
                s_list[right], s_list[left] = s_list[left], s_list[right]
                left += 1
                right -= 1
            
            count += 2 * k
        
        return "".join(s_list)