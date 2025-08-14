class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        set_candy = set(candyType)
        allowed = len(candyType) // 2

        return min(len(set_candy), allowed)