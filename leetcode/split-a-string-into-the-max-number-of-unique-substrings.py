class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        maxCount = 0
        subset = set()

        def dfs(idx):
            nonlocal maxCount
            if (idx >= len(s)):
                maxCount = max(maxCount, len(subset))
                return
            
            for jdx in range(idx, len(s)):
                val = s[idx : jdx + 1]

                if (val in subset):
                    continue

                subset.add(val)
                dfs(jdx + 1)
                subset.remove(val)
        
        dfs(0)
        return maxCount