class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        final = []
        left = 0

        for right in range(len(nums)):
            while len(queue) > 0 and nums[queue[-1]] < nums[right]:
                queue.pop()
            
            queue.append(right)

            if (left > queue[0]):
                queue.popleft()
            
            if ((right + 1) >= k):
                final.append(nums[queue[0]])
                left += 1
        
        return final