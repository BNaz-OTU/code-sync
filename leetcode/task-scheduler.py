class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        heap = []
        queue = deque()

        for task in tasks:
            if (task not in hashMap):
                hashMap[task] = 0
            
            hashMap[task] += 1
        
        # print(hashMap)

        for task, count in hashMap.items():
            heappush(heap, [-count, task])
        
        time = 0
        while len(heap) > 0 or len(queue) > 0:

            if (len(queue) > 0 and queue[0][0] == time):
                _, count, task = queue.popleft()
                heappush(heap, [count, task])

            
            if (len(heap) > 0):
                count, task = heappop(heap)

                if (count + 1 < 0):
                    queue.append([time + n + 1, count + 1, task])
            
            time += 1
        
        return time