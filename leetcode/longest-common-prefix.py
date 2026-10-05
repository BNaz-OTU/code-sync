class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        for idx in range(len(strs[0])):
            char = strs[0][idx]
            for string in strs:
                if (idx >= len(string) or char != string[idx]):
                    return prefix

            prefix += char
        
        return prefix