class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_h = sorted(heights)
        count = 0

        for idx in range(len(heights)):
            if (sort_h[idx] != heights[idx]):
                count += 1
        
        return count