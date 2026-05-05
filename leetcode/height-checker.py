class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        sort_h = sorted(heights)
        counter = 0

        for idx in range(len(heights)):
            if (sort_h[idx] != heights[idx]):
                counter += 1
        
        return counter