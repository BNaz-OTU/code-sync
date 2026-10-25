class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashmap = {}

        for string in strs:
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1
            
            if (tuple(count) not in hashmap):
                hashmap[tuple(count)] = []

            hashmap[tuple(count)].append(string)
        
        return list(hashmap.values())