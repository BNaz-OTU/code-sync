class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        left = 0
        visit = deque()
        counter = 0
        sumVal = 0

        for right in range(len(arr)):
            barrier = (right - left + 1)
            if (barrier > k):
                sumVal -= arr[left]
                left += 1
                
            sumVal += arr[right]

            barrier = (right - left + 1)
            if (barrier == k and (sumVal / barrier) >= threshold):
                counter += 1
        
        return counter