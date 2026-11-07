class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}
        final = []

        for string in strs:
            arr = [0] * 26

            for char in string:
                idx = ord(char) - ord('a')
                arr[idx] += 1
            
            if (str(arr) not in hashmap):
                hashmap[str(arr)] = []
            
            hashmap[str(arr)].append(string)
        
        for value in hashmap.values():
            final.append(value)
        
        return final