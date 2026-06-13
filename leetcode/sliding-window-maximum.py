class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()
        final = []
        left, right = 0, 0

        while right < len(nums):
            # Pop smaller values from 'queue'
            while queue and nums[queue[-1]] < nums[right]:
                queue.pop()
            
            queue.append(right)

            # Remove left val from window
            if (left > queue[0]):
                queue.popleft()
            
            if (right + 1) >= k:
                final.append(nums[queue[0]])
                left += 1
            
            right += 1
        
        return final