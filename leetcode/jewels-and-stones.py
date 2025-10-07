class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0

        for val in stones:
            if (val in jewels):
                count += 1
        
        return count