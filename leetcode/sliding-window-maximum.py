class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        final = []
        queue = deque()

        left = 0
        for right in range(len(nums)):
            # print(right, queue)
            while (len(queue) > 0 and nums[queue[-1]] < nums[right]):
                queue.pop()

            queue.append(right)
            
            if (right >= k - 1):
                final.append(nums[queue[0]])

                if (queue[0] <= left):
                    queue.popleft()

                left += 1
        
            # print(right, queue)
            # print()
        return final