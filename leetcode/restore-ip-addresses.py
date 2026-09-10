class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        final = []

        if (len(s) > 12):
            return []
        
        def dfs(periodCount, text, idx):
            if (periodCount == 4 and idx == len(s)):
                final.append(text[:-1])
                return
            
            if periodCount > 4:
                return
            
            for jdx in range(idx, min(idx + 3, len(s))): 
                if (int(s[idx : jdx + 1]) < 256 and (idx == jdx or s[idx] != "0")):                
                    dfs(periodCount + 1, text + s[idx : jdx + 1] + ".", jdx + 1)
        
        dfs(0, "", 0)
        return final