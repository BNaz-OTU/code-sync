class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if (len(s1) > len(s2)):
            return False

        s1Count = [0] * 26
        s2Count = [0] * 26

        for idx in range(len(s1)):
            s1Let = ord(s1[idx]) - ord('a')
            s2Let = ord(s2[idx]) - ord('a')

            s1Count[s1Let] += 1
            s2Count[s2Let] += 1
        
        matches = 0
        for idx in range(26):
            if (s1Count[idx] == s2Count[idx]):
                matches += 1
        
        # print(matches)
        left = 0
        for idx in range(len(s1), len(s2)):
            if (matches == 26):
                return True

            # print(matches)

            s2Let = ord(s2[idx]) - ord('a')
            s2Count[s2Let] += 1

            if (s2Count[s2Let] == s1Count[s2Let]):
                matches += 1
            elif (s2Count[s2Let] == s1Count[s2Let] + 1):
                matches -= 1
            
            s2LetPrev = ord(s2[left]) - ord('a')
            s2Count[s2LetPrev] -= 1

            if (s2Count[s2LetPrev] == s1Count[s2LetPrev]):
                matches += 1
            elif (s2Count[s2LetPrev] == s1Count[s2LetPrev] - 1):
                matches -= 1
            
            left += 1


        return matches == 26