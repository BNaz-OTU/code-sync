class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        count = 0
        apple_sum = sum(apple)
        capacity.sort()

        while apple_sum > 0:
            apple_sum -= capacity.pop()
            count += 1
        
        return count