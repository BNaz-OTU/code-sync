class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0

        while n > 0:
            remainder = n % 2
            n = n // 2

            count += remainder

        return count