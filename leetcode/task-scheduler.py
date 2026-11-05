class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        hashmap = {}

        for task in tasks:
            if (task not in hashmap):
                hashmap[task] = 0
            
            hashmap[task] += 1
        
        heap = []
        for key, val in hashmap.items():
            heappush(heap, -val)
        
        print(heap)
        time = 0
        queue = deque()

        while len(heap) > 0 or len(queue) > 0:
            time += 1

            if (len(heap) > 0):
                remain = 1 + heappop(heap)

                if remain != 0:
                    queue.append([remain, time + n])
            
            if len(queue) > 0 and queue[0][1] == time:
                val = queue.popleft()[0]
                heappush(heap, val)
        
        return time