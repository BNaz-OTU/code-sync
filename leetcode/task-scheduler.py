class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        heap = []
        queue = deque()

        for task in tasks:
            if (task not in hashMap):
                hashMap[task] = 0
            
            hashMap[task] += 1
        
        for task, count in hashMap.items():
            heappush(heap, [-count, task])
        
        time = 0
        while heap or queue:
            # print(time)
            # print(heap)
            # print(queue)
            # print()
            if (len(queue) > 0 and queue[0][0] == time):
                _, count, task = queue.popleft()

                if (count < 0):
                    heappush(heap, [count, task])

            if (len(heap) > 0):
                count, task = heappop(heap)
                if (count + 1 != 0):
                    queue.append([time + n + 1, count + 1, task])
            
            time += 1
        
        return time