class Solution:
    def maxLength(self, arr: list[str]) -> int:
        theSet = set()

        def overlap(charSet, s):
            prev = set()
            for c in s:
                if c in charSet or c in prev:
                    return True
                prev.add(c)
            
            return False
        
        def dfs(idx):
            if (idx == len(arr)):
                return len(theSet)
            
            res = 0
            if (not overlap(theSet, arr[idx])):
                for char in arr[idx]:
                    theSet.add(char)
                res = dfs(idx + 1)
                for char in arr[idx]:
                    theSet.remove(char)
            
            return max(res, dfs(idx + 1))
        
        return dfs(0)