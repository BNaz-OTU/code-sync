class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False
            
        alpha1 = [0] * 26
        alpha2 = [0] * 26
        matches = 0

        for idx in range(len(s1)):
            alpha1[ord(s1[idx]) - ord('a')] += 1
            alpha2[ord(s2[idx]) - ord('a')] += 1
        
        for idx in range(26):
            if alpha1[idx] == alpha2[idx]:
                matches += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True
            
            # RIGHT
            idx = ord(s2[right]) - ord('a')
            alpha2[idx] += 1

            if alpha1[idx] == alpha2[idx]:
                matches += 1

            elif alpha1[idx] + 1 == alpha2[idx]:
                matches -= 1
            
            # LEFT
            idx = ord(s2[left]) - ord('a')
            alpha2[idx] -= 1

            if alpha1[idx] == alpha2[idx]:
                matches += 1

            elif alpha1[idx] - 1 == alpha2[idx]:
                matches -= 1
            
            left += 1
        
        return matches == 26