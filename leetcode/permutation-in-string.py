class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        arr1, arr2 = [0] * 26, [0] * 26
        for idx in range(len(s1)):
            charS1, charS2 = s1[idx], s2[idx]

            idx1 = ord(charS1) - ord('a')
            idx2 = ord(charS2) - ord('a')

            arr1[idx1] += 1
            arr2[idx2] += 1
        
        matches = 0
        for idx in range(26):
            if (arr1[idx] == arr2[idx]):
                matches += 1
        
        if matches == 26:
            return True
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            l_char, r_char = s2[left], s2[right]
            l_idx, r_idx = ord(l_char) - ord('a'), ord(r_char) - ord('a')

            arr2[r_idx] += 1
            if (arr2[r_idx] == arr1[r_idx]):
                matches += 1
            
            elif (arr2[r_idx] == arr1[r_idx] + 1):
                matches -= 1

            arr2[l_idx] -= 1
            if (arr2[l_idx] == arr1[l_idx]):
                matches += 1
            
            elif (arr2[l_idx] == arr1[l_idx] - 1):
                matches -= 1
            
            left += 1
            
        
        return matches == 26