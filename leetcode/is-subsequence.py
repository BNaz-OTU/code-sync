class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_idx = 0
        t_idx = 0

        while (s_idx < len(s) and t_idx < len(t)):
            print('S:', s_idx, 'T', t_idx)
            if (s[s_idx] == t[t_idx]):
                s_idx += 1
            t_idx += 1
        
        # print(s_idx)
        if (s_idx == len(s)):
            return True
        else:
            return False