class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        idx = 0
        flag = False

        smallest = float("inf")
        for string in strs:
            smallest = min(smallest, len(string))
        
        while idx < smallest:
            prefix += strs[0][idx]
            for string in strs:
                if string[idx] != prefix[-1]:
                    flag = True
                    break
            
            if (flag):
                prefix = prefix[:-1]
                break
                
            idx += 1
        
        return prefix