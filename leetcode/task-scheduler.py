class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashTask = {}
        queue = deque()

        for task in tasks:
            if task not in hashTask:
                hashTask[task] = 0
            
            hashTask[task] += 1
        
        heap = []

        for task, count in hashTask.items():
            heappush(heap, [-count, task])
        
        time = 0
        while heap or queue:
            # print(f"Heap: {heap}")
            # print(f"Queue: {queue}")
            # print(time)
            # print()
            if queue and queue[0][0] == time:
                _, miniContainer = queue.popleft()
                heappush(heap, [miniContainer[0], miniContainer[1]])
            
            if heap:
                count, task = heappop(heap)
                count += 1
                if (count != 0):  
                    queue.append([time + n + 1, (count, task)])

            time += 1
        
        return time